## 3.2 Retry policy

A "failed request" means any request that returns a 5xx status or times out after 30 seconds. The
client MUST retry a failed request up to three (3) times, except when the server returns a 4xx
status other than 429, in which case it MUST NOT retry. Retries should use exponential backoff
(base 100 ms) to avoid overwhelming the server.
