import typer
import copier
import os
from pathlib import Path

app = typer.Typer()

@app.command()
def create(
    project_name: str = typer.Argument(..., help="Name of the project to create"),
    template_path: str = typer.Option(None, "--template", "-t", help="Path to the template"),
    database: str = typer.Option("postgres", "--database", "-d", help="Database to use (postgres or mongodb)"),
    enable_langsmith: bool = typer.Option(True, "--langsmith/--no-langsmith", help="Enable LangSmith"),
    python_version: str = typer.Option("3.11", "--python", "-p", help="Python version"),
    interactive: bool = typer.Option(False, "--interactive/--no-interactive", help="Enable interactive mode")
):
    """
    Scaffold a new FastAPI-based GenAI project.
    """
    if template_path is None:
        # Resolve the built-in template path
        template_path = str((Path(__file__).parent.parent / "template/").resolve())
    else:
        template_path = str(Path(template_path).resolve())

    typer.echo(f"🚀 Creating project '{project_name}'...")
    typer.echo(f"  - Template: {template_path}")
    typer.echo(f"  - Destination: {Path(project_name).resolve()}")
    
    # Run copier to generate the project
    try:
        copier.run_copy(
            template_path,
            str(Path(project_name).resolve()),
            data={
                "project_name": project_name,
                "database": database,
                "enable_langsmith": enable_langsmith,
                "python_version": python_version,
                "description": f"FastAPI-based GenAI microservice for {project_name}"
            },
            overwrite=True,
            quiet=not interactive,
        )
        typer.echo(f"✅ Project '{project_name}' created successfully!")
    except Exception as e:
        typer.echo(f"❌ Error creating project: {e}", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
