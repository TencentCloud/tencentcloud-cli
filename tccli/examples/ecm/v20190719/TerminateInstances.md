**Example 1: 销毁实例**

销毁实例

Input: 

```
tccli ecm TerminateInstances --cli-unfold-argument  \
    --TerminateDelay true \
    --InstanceIdSet ein-197252sp ein-187232ag \
    --TerminateTime '2019-08-01 18:32:56'
```

Output: 
```
{
    "Response": {
        "RequestId": "df348fj3-03g7-4ss0-y7sj-78e2322a3242"
    }
}
```

