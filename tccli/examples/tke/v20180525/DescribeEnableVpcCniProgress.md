**Example 1: 查看开启vpc-cni的任务进度**

用户调用EnableVpcCniNetworkType给GR集群附加vpc-cni网络能力，会创建一个异步任务。本接口用于查询该异步任务的进度

Input: 

```
tccli tke DescribeEnableVpcCniProgress --cli-unfold-argument  \
    --ClusterId xx
```

Output: 
```
{
    "Response": {
        "Status": "xx",
        "ErrorMessage": "xxxx",
        "RequestId": "xx"
    }
}
```

