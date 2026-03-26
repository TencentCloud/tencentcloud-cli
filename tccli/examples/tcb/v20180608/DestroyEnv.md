**Example 1: 云开发环境退款**

用于给云开发环境退款。
退款后，环境会进入隔离期。通过接口 [DescribeBillingInfo](https://cloud.tencent.com/document/product/876/94390) 可以查到环境的计费状态。

Input: 

```
tccli tcb DestroyEnv --cli-unfold-argument  \
    --EnvId my-envid-xu94jkgjdlkjlsd
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

**Example 2: 彻底删除隔离期的环境**

用于彻底删除已进入隔离期的环境。需要指定参数 IsForce = true 。
注意⚠️
  环境被删除之后，任何数据都将无法找回，请谨慎操作。

Input: 

```
tccli tcb DestroyEnv --cli-unfold-argument  \
    --EnvId my-envid-xu94jkgjdlkjlsd \
    --IsForce True
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

