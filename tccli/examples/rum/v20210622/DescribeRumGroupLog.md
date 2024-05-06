**Example 1: 2312**



Input: 

```
tccli rum DescribeRumGroupLog --cli-unfold-argument  \
    --OrderBy asc \
    --ID 1 \
    --Limit 1 \
    --GroupField  \
    --StartTime 1 \
    --Query 1 \
    --EndTime 1 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "RequestId": "81a43a52-d00f-462a-82da-89841117f4ca",
        "Result": ""
    }
}
```

**Example 2: 获取日志列表**



Input: 

```
tccli rum DescribeRumGroupLog --cli-unfold-argument  \
    --OrderBy "desc" \
    --StartTime "1" \
    --Limit 10 \
    --Query "*" \
    --EndTime "20" \
    --ID 10 \
    --Page 1 \
    --GroupField date
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

