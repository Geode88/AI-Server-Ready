from pathlib import Path


def summarize_tree(root: str = '.') -> dict:
    base = Path(root)
    if not base.exists():
        return {'exists': False, 'root': str(base)}

    files = [p for p in base.rglob('*') if p.is_file()]
    top_level = sorted([p.name for p in base.iterdir()]) if base.is_dir() else []
    return {
        'exists': True,
        'root': str(base.resolve()),
        'file_count': len(files),
        'top_level': top_level[:25],
        'python_files': sum(1 for p in files if p.suffix == '.py'),
        'markdown_files': sum(1 for p in files if p.suffix.lower() == '.md'),
    }


if __name__ == '__main__':
    print(summarize_tree())
