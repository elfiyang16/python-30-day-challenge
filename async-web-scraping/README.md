asyncio is a library to write concurrent code using the async/await syntax.

```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())
```

This module provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives. Here is a more detailed list of the package contents:

a pluggable event loop with various system-specific implementations;

transport and protocol abstractions (similar to those in Twisted);

concrete support for TCP, UDP, SSL, subprocess pipes, delayed calls, and others (some may be system-dependent);

a Future class that mimics the one in the concurrent.futures module, but adapted for use with the event loop;

coroutines and tasks based on yield from (PEP 380), to help write concurrent code in a sequential fashion;

cancellation support for Futures and coroutines;

synchronization primitives for use between coroutines in a single thread, mimicking those in the threading module;

an interface for passing work off to a threadpool, for times when you absolutely, positively have to use a library that makes blocking I/O calls.