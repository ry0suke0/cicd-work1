from __future__ import annotations

def normalize_mode(mode: str) -> str:
    """Python 3.10+ の match/case を使う（CIが3.8だとSyntaxErrorになる）"""
    match mode.strip().lower():
        case "fast" | "f":
            return "fast"
        case "safe" | "s":
            return "safe"
        case _:
            return "safe"
