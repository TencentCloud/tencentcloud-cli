**Example 1: 获取集群管理员角色**

CAM管理员子账户，拥有此action的权限之后，可以通过该接口获取集群管理员角色，访问kubernetes集群内资源。

Input: 

```
tccli tke AcquireClusterAdminRole --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe
```

Output: 
```
{
    "Response": {
        "RequestId": "24564577-a642-4164-8752-4668d4ca8886"
    }
}
```

