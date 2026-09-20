**Example 1: 取消 Version**

PREPARING / PENDING_APPROVAL → CANCELED，仅可取消非 Stable Version。

Input: 

```
tccli ags CancelRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

