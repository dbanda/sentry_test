import sentry_sdk
sentry_sdk.init(
    dsn="https://572acdfc06aa47db8e1dd6fa6b028539@o1297826.ingest.sentry.io/6689936",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


# introduce error
#division_by_zero = 1 / 0


