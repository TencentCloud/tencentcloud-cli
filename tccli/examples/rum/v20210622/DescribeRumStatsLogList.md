**Example 1: 1212**



Input: 

```
tccli rum DescribeRumStatsLogList --cli-unfold-argument  \
    --Query 1 \
    --EndTime 1 \
    --Limit 1 \
    --ID 1 \
    --StartTime 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7987e9a1-cece-4468-b104-cd239f2f6cd6",
        "Result": ""
    }
}
```

**Example 2: 获取日志列表**



Input: 

```
tccli rum DescribeRumStatsLogList --cli-unfold-argument  \
    --StartTime "1" \
    --Limit 10 \
    --Query "*" \
    --EndTime "20" \
    --ID 10
```

Output: 
```
{
    "Response": {
        "Result": "Traceback (most recent call last):\n  File \"/opt/app-root/lib64/python3.8/site-packages/tornado/web.py\", line 1763, in _execute\n    result = self.prepare()\n  File \"/opt/app-root/lib64/python3.8/site-packages/tornado/web.py\", line 2538, in prepare\n    raise HTTPError(self._status_code)\ntornado.web.HTTPError: HTTP 404: Not Found\n",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

