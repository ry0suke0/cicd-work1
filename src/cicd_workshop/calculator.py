from __future__ import annotations
from .utils import normalize_mode

def add(a: int, b: int, mode: str = "safe") -> int:
    """本来は a + b を返すべきだが、わざと +1 してしまっているバグ。"""
    _ = normalize_mode(mode)  # utils を import しているので CI(3.8)で確実に落ちる
    return a + b + 1  # BUG: off-by-one

def multiply(a: int, b: int, mode: str = "safe") -> int:
    """本来は負数も含めて掛け算できる想定だが、わざと負数を拒否しているバグ。"""
    _ = normalize_mode(mode)
    if a < 0 or b < 0:
        raise ValueError("負の数はサポートしていません（わざとバグ）")
    return a * b
