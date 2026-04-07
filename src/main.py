from pathlib import Path
import sys
import yaml
from rich.console import Console

console = Console()


def load_settings() -> dict:
    cfg = Path('config/settings.example.yaml')
    if not cfg.exists():
        return {}
    return yaml.safe_load(cfg.read_text(encoding='utf-8')) or {}


def ensure_workspace(settings: dict) -> None:
    paths = settings.get('paths', {})
    for key in ('workspace', 'state'):
        p = Path(paths.get(key, key))
        p.mkdir(parents=True, exist_ok=True)
        console.print(f'[green]ready[/green] {key}: {p.resolve()}')


def main() -> int:
    settings = load_settings()
    console.print('[bold cyan]AI-Server-Ready[/bold cyan]')
    console.print('Local-first control plane initialized.')
    ensure_workspace(settings)
    console.print('Next recommended step: add repo audit, ingestion, and reporting modules.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
