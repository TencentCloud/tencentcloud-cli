**Example 1: 获取个人运行环境详情**

获取个人运行环境详情

Input: 

```
tccli wedata GetCodeWorkspace --cli-unfold-argument  \
    --WorkspaceId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "251436191",
            "ClusterInfo": {
                "ClusterId": "",
                "GatewayAddr": "21.215.198.151",
                "Region": "ap-guangzhou",
                "SubnetId": "subnet-ou4ow4nu",
                "VpcId": "vpc-jlm043wl"
            },
            "CodeWorkspaceId": "f99fca80-5f8e-41d8-b7c0-7db4dafe2099",
            "CreateTime": "1762500297051",
            "CreateUserUin": "700002164618",
            "DebugInfo": "",
            "EnvConfigs": [
                {
                    "Name": "KERNEL_SAML_SUB",
                    "Value": "700002164618"
                },
                {
                    "Name": "WORKSPACE_TYPE",
                    "Value": "USER_TYPE"
                },
                {
                    "Name": "USER_APPID",
                    "Value": "251436191"
                },
                {
                    "Name": "USER_UIN",
                    "Value": "700002164618"
                },
                {
                    "Name": "OWNER_UIN",
                    "Value": "700002164618"
                },
                {
                    "Name": "REGION",
                    "Value": "ap-beijing"
                },
                {
                    "Name": "WEDATA_PROJECT_ID",
                    "Value": "1470547050521227264"
                },
                {
                    "Name": "PROFILE_ENV",
                    "Value": "dev"
                },
                {
                    "Name": "LOCAL_CBS_MOUNT_PATH",
                    "Value": "/data/cbs"
                },
                {
                    "Name": "WORKSPACE_TIMEZONE",
                    "Value": "Asia/Shanghai"
                },
                {
                    "Name": "CFS_MOUNT_SHARE_DIR",
                    "Value": "/data/wedata/share/1470547050521227264"
                },
                {
                    "Name": "POD_MOUNT_SHARE_DIR",
                    "Value": "/Workspace"
                },
                {
                    "Name": "CFS_MOUNT_GIT_DIR",
                    "Value": "/data/wedata/git/1470547050521227264/700002164618"
                },
                {
                    "Name": "POD_MOUNT_GIT_DIR",
                    "Value": "/GitFolder"
                }
            ],
            "HasInitialized": false,
            "Id": "44",
            "Image": {
                "Image": "ccr.ccs.tencentyun.com/wedata3/wedata-ude-ide",
                "ImageTag": "dev30-wedata-ude-ide-dfc5383b341731a3a0630df8992211d62507b849-42"
            },
            "InstanceId": "20251107152457034210",
            "NetworkInfo": {
                "CsVIp": "21.78.37.177",
                "CsVPort": 8080,
                "JsVIp": "21.78.37.177",
                "JsVPort": 8889
            },
            "NewImageVersion": "dev30-wedata-ude-ide-dfc5383b341731a3a0630df8992211d62507b849-42",
            "OwnerUin": "700002164618",
            "ScriptStorageConfig": {
                "CommonCFSMountPath": "/data/wedata/share/1470547050521227264",
                "CommonPodMountPath": "/Workspace",
                "GitCFSMountPath": "/data/wedata/git/1470547050521227264/700002164618",
                "GitMountPath": "/GitFolder",
                "PersonalCFSMountPath": "",
                "PersonalPodMountPath": "",
                "RecycleBinCFSMountPath": "/data/wedata/trash/1470547050521227264/700002164618",
                "RecycleBinMountPath": "/data/wedata/trash"
            },
            "SpecificationInfo": {
                "CpuCores": 4000,
                "CpuCoresLimit": 8000,
                "MemorySize": 8192,
                "MemorySizeLimit": 16384
            },
            "Stage": "updata_workload_wait",
            "Status": "UPDATING",
            "Type": "USER_TYPE",
            "UpdateTime": "1762768192000",
            "WorkspaceId": "1470547050521227264"
        },
        "RequestId": "a19fe2ec-5528-4b1b-b7bb-a5cf2ecdf6c1"
    }
}
```

