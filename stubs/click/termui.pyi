from ._compat import DEFAULT_COLUMNS as DEFAULT_COLUMNS, WIN as WIN, get_winterm_size as get_winterm_size, isatty as isatty, raw_input as raw_input, string_types as string_types, strip_ansi as strip_ansi, text_type as text_type
from .exceptions import Abort as Abort, UsageError as UsageError
from .globals import resolve_color_default as resolve_color_default
from .types import convert_type as convert_type
from .utils import echo as echo
from typing import Any, Optional

visible_prompt_func = raw_input

def hidden_prompt_func(prompt: Any): ...
def prompt(text: Any, default: Optional[Any] = ..., hide_input: bool = ..., confirmation_prompt: bool = ..., type: Optional[Any] = ..., value_proc: Optional[Any] = ..., prompt_suffix: str = ..., show_default: bool = ..., err: bool = ...): ...
def confirm(text: Any, default: bool = ..., abort: bool = ..., prompt_suffix: str = ..., show_default: bool = ..., err: bool = ...): ...
def get_terminal_size(): ...
def echo_via_pager(text: Any, color: Optional[Any] = ...): ...
def progressbar(iterable: Optional[Any] = ..., length: Optional[Any] = ..., label: Optional[Any] = ..., show_eta: bool = ..., show_percent: Optional[Any] = ..., show_pos: bool = ..., item_show_func: Optional[Any] = ..., fill_char: str = ..., empty_char: str = ..., bar_template: str = ..., info_sep: str = ..., width: int = ..., file: Optional[Any] = ..., color: Optional[Any] = ...): ...
def clear() -> None: ...
def style(text: Any, fg: Optional[Any] = ..., bg: Optional[Any] = ..., bold: Optional[Any] = ..., dim: Optional[Any] = ..., underline: Optional[Any] = ..., blink: Optional[Any] = ..., reverse: Optional[Any] = ..., reset: bool = ...): ...
def unstyle(text: Any): ...
def secho(text: Any, file: Optional[Any] = ..., nl: bool = ..., err: bool = ..., color: Optional[Any] = ..., **styles: Any): ...
def edit(text: Optional[Any] = ..., editor: Optional[Any] = ..., env: Optional[Any] = ..., require_save: bool = ..., extension: str = ..., filename: Optional[Any] = ...): ...
def launch(url: Any, wait: bool = ..., locate: bool = ...): ...
def getchar(echo: bool = ...): ...
def pause(info: str = ..., err: bool = ...) -> None: ...
