import sentry_sdk
sentry_sdk.init(
    dsn="https://01ad21ab25274d3986838d47ccf79f5a@o1353710.ingest.sentry.io/6636539",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


# introduce error
#division_by_zero = 1 / 0
print(hello)


