**Example 1: GetServicePodLogs**



Input: 

```
tccli hai GetServicePodLogs --cli-unfold-argument  \
    --ServiceId svc-6rt0ffqx \
    --PodName svc-6rt0ffqx-0 \
    --TailLines 100
```

Output: 
```
{
    "Response": {
        "LogLines": [
            "[2025-09-03 14:58:30] INFO:     10.0.7.10:60394 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 14:58:59] INFO:     10.0.7.10:60618 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 14:58:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 14:59:00] INFO:     10.0.7.10:60620 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 14:59:29] INFO:     10.0.7.10:60812 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 14:59:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 14:59:30] INFO:     10.0.7.10:60814 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 14:59:59] INFO:     10.0.7.10:32772 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 14:59:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:00:00] INFO:     10.0.7.10:32774 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:00:29] INFO:     10.0.7.10:33006 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:00:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:00:30] INFO:     10.0.7.10:33008 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:00:59] INFO:     10.0.7.10:33204 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:00:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:01:00] INFO:     10.0.7.10:33206 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:01:29] INFO:     10.0.7.10:33430 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:01:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:01:30] INFO:     10.0.7.10:33428 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:01:59] INFO:     10.0.7.10:33624 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:01:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:02:00] INFO:     10.0.7.10:33626 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:02:29] INFO:     10.0.7.10:33852 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:02:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:02:30] INFO:     10.0.7.10:33854 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:02:59] INFO:     10.0.7.10:34056 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:02:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:03:00] INFO:     10.0.7.10:34058 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:03:29] INFO:     10.0.7.10:34286 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:03:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:03:30] INFO:     10.0.7.10:34288 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:03:59] INFO:     10.0.7.10:34508 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:03:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:04:00] INFO:     10.0.7.10:34510 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:04:29] INFO:     10.0.7.10:34716 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:04:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:04:30] INFO:     10.0.7.10:34714 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:04:59] INFO:     10.0.7.10:34916 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:04:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:05:00] INFO:     10.0.7.10:34914 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:05:29] INFO:     10.0.7.10:35142 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:05:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:05:30] INFO:     10.0.7.10:35140 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:05:59] INFO:     10.0.7.10:35358 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:05:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:06:00] INFO:     10.0.7.10:35360 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:06:29] INFO:     10.0.7.10:35560 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:06:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:06:30] INFO:     10.0.7.10:35558 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:06:59] INFO:     10.0.7.10:35754 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:06:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:07:00] INFO:     10.0.7.10:35752 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:07:29] INFO:     10.0.7.10:35982 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:07:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:07:30] INFO:     10.0.7.10:35980 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:07:59] INFO:     10.0.7.10:36176 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:07:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:08:00] INFO:     10.0.7.10:36174 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:08:29] INFO:     10.0.7.10:36420 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:08:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:08:30] INFO:     10.0.7.10:36422 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:08:59] INFO:     10.0.7.10:36620 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:08:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:09:00] INFO:     10.0.7.10:36618 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:09:29] INFO:     10.0.7.10:36842 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:09:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:09:30] INFO:     10.0.7.10:36844 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:09:59] INFO:     10.0.7.10:37040 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:09:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:10:00] INFO:     10.0.7.10:37038 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:10:29] INFO:     10.0.7.10:37266 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:10:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:10:30] INFO:     10.0.7.10:37264 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:10:59] INFO:     10.0.7.10:37454 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:10:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:11:00] INFO:     10.0.7.10:37456 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:11:29] INFO:     10.0.7.10:37680 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:11:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:11:30] INFO:     10.0.7.10:37682 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:11:59] INFO:     10.0.7.10:37902 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:11:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:12:00] INFO:     10.0.7.10:37904 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:12:29] INFO:     10.0.7.10:38100 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:12:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:12:30] INFO:     10.0.7.10:38098 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:12:59] INFO:     10.0.7.10:38296 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:12:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:13:00] INFO:     10.0.7.10:38298 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:13:29] INFO:     10.0.7.10:38524 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:13:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:13:30] INFO:     10.0.7.10:38522 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:13:59] INFO:     10.0.7.10:38742 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:13:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:14:00] INFO:     10.0.7.10:38740 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:14:29] INFO:     10.0.7.10:38942 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:14:29] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:14:30] INFO:     10.0.7.10:38944 - \"GET /health_generate HTTP/1.1\" 200 OK",
            "[2025-09-03 15:14:59] INFO:     10.0.7.10:39138 - \"GET /health HTTP/1.1\" 200 OK",
            "[2025-09-03 15:14:59] Prefill batch. #new-seq: 1, #new-token: 1, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0",
            "[2025-09-03 15:15:00] INFO:     10.0.7.10:39140 - \"GET /health_generate HTTP/1.1\" 200 OK"
        ],
        "RequestId": "64015e14-a860-4c62-bd4d-6678b2498115"
    }
}
```

