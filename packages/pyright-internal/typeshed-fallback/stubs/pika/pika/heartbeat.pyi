from logging import Logger

LOGGER: Logger

class HeartbeatChecker:
    def __init__(self, connection, timeout) -> None: ...
    @property
    def bytes_received_on_connection(self): ...
    @property
    def connection_is_idle(self): ...
    def received(self) -> None: ...
    def stop(self) -> None: ...
