from prometheus_client import Counter, Gauge

RECEIVED_RAW_REQUEST_CNTR = Counter(
    "RECEIVED_RAW_REQUEST_CNTR", "Number of received raw request"
)
RAW_REQUEST_PARCED_SUCCESS_CNTR = Counter(
    "RAW_REQUEST_PARCED_SUCCESS_CNTR", "Number of raw request parsed successfully"
)
RAW_REQUEST_PARCED_ERROR_CNTR = Counter(
    "RAW_REQUEST_PARCED_ERROR_CNTR", "Number of raw request parsed with error"
)
RAW_REQUEST_SENT_TO_KAFKA_SUCCESS_CNTR = Counter(
    "RAW_REQUEST_SENT_TO_KAFKA_SUCCESS_CNTR",
    "Number of raw request sent to kafka sucessfully",
)
RAW_REQUEST_SENT_TO_KAFKA_ERROR_CNTR = Counter(
    "RAW_REQUEST_SENT_TO_KAFKA_ERROR_CNTR",
    "Number of raw request sent to kafka with error",
)

# Persist store metrics
PERSIST_METRIC_GAUGE = Gauge(
    "PERSIST_METRIC_GAUGE", "Custom persist metric", labelnames=["metric_name"]
)
