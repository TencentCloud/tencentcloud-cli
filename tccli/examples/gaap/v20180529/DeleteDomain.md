**Example 1: Deleting a Forwarding Rule Based on Domain Names**



Input: 

```
tccli gaap DeleteDomain --cli-unfold-argument  \
    --ListenerId 0 \
    --Domain a.a.com \
    --Force 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

