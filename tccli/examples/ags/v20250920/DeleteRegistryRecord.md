**Example 1: 删除单个 Version**

传入 VersionId 时只删除该 Version（软删除）；Stable 指向的 Version 或最后一个 Approved Version 不允许删除。

Input: 

```
tccli ags DeleteRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

**Example 2: 软删除整个 Record**

省略 VersionId 时对整个 Record 进行软删除。

Input: 

```
tccli ags DeleteRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

