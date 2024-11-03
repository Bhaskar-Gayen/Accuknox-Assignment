# Django Signal Synchronous Execution Example

By default, Django signals are executed synchronously. When a signal is sent, Django calls all connected receivers immediately before the signal-sending function returns. This synchronous behavior can be demonstrated by tracking the execution order.

This example demonstrates the **synchronous execution** of Django signals.

## Overview

In this example:

1. A `UserProfile` instance is created, which triggers the `post_save` signal.
2. The signal receiver, `welcome_user`, introduces a **2-second delay** to simulate synchronous processing.
3. This delay affects the total execution time, demonstrating that the signal is processed synchronously within the main function.
