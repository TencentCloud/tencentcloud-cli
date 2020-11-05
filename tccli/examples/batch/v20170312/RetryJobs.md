**Example 1: Retrying Jobs**

When some task instances fail in a task, only the failing instances will be retried, and the succeeding ones will not be processed.

Input: 

```
tccli batch RetryJobs --cli-unfold-argument  \
    --JobIds job-rybewp57 job-97zcl3wt
```

Output: 
```
{
    "Response": {
        "RequestId": "970e5a9f-2963-436c-8dad-4847360676f7"
    }
}
```

