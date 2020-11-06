**Example 1: Uninstalling plugins in batches**



Input: 

```
tccli es UpdatePlugins --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --RemovePluginList analysis-qq sql
```

Output: 
```
{
    "Response": {
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

**Example 2: Installing plugins in batches**



Input: 

```
tccli es UpdatePlugins --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --InstallPluginList analysis-qq sql
```

Output: 
```
{
    "Response": {
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

