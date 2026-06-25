**Example 1: 创建 DB Custom 节点（保持镜像的原始登录方式）**



Input: 

```
tccli dbdc CreateDBCustomNodes --cli-unfold-argument  \
    --Zone ap-shanghai-5 \
    --ImageId img-2htjru6l \
    --VpcId vpc-3kmj79e2 \
    --SubnetId subnet-pqebu78d \
    --Period 1 \
    --NodeType DB.AT5.8XLARGE128 \
    --NodeCount 1 \
    --LoginSettings.KeepImageLogin true \
    --AutoRenew 2 \
    --NodeName 私有镜像自带SSHKey
```

Output: 
```
{
    "Response": {
        "NodeIds": [
            "dbcn-o2q3rj8t"
        ],
        "TaskId": 756,
        "RequestId": "e7026ac1-125f-4e74-ae38-029ad41defe6"
    }
}
```

**Example 2: 创建 DB Custom 节点（通过密钥登录节点）**



Input: 

```
tccli dbdc CreateDBCustomNodes --cli-unfold-argument  \
    --Zone ap-shanghai-5 \
    --ImageId img-1tmhysjj \
    --VpcId vpc-3kmj79e2 \
    --SubnetId subnet-pqebu78d \
    --Period 1 \
    --NodeType DB.AT5.8XLARGE128 \
    --NodeCount 1 \
    --LoginSettings.KeyIds skey-48hbnu45 \
    --AutoRenew 2 \
    --NodeName 5*SSHKeyID+公共镜像
```

Output: 
```
{
    "Response": {
        "NodeIds": [
            "dbcn-z4z0rbc9"
        ],
        "TaskId": 746,
        "RequestId": "7203009a-4d1e-42e1-a394-83f118bbc995"
    }
}
```

