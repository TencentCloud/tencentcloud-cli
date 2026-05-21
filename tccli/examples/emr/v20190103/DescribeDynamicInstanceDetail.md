**Example 1: DynamicInstance 详细信息**



Input: 

```
tccli emr DescribeDynamicInstanceDetail --cli-unfold-argument  \
    --InstanceId emr-a2jqs6n3 \
    --RayClusterId 28
```

Output: 
```
{
    "Response": {
        "CreateTime": "2025-12-27 16:43:18",
        "DashboardUrl": "http://43.141.243.208/raycluster",
        "HeadGroupSpec": {
            "Cpu": 1,
            "Env": [
                {
                    "Name": "testkey",
                    "Value": "testval"
                }
            ],
            "Gpu": 0,
            "GpuType": "",
            "GroupType": "HeadGroup",
            "Labels": [
                {
                    "Name": "label-key-01",
                    "Value": "label-val-01"
                }
            ],
            "MaxNodes": 0,
            "MemSize": 2,
            "MinNodes": 0,
            "Name": "headGroup",
            "PersistentVolume": {
                "CBSVolumes": [],
                "CFSVolumes": [],
                "COSVolumes": [],
                "StorageVolumeDetail": [],
                "StorageVolumeName": [],
                "VolumeMounts": []
            },
            "PodCount": 2,
            "ResourceLabels": "{\"Custom1\":1,\"Custom2\":5}",
            "Scheduler": "{\"nodeSelector\":{\"kubernetes.io/hostname\":\"10.0.1.61\"},\"nodeAffinity\":null}",
            "StorageConfigEnabled": false,
            "Tolerations": [
                {
                    "Key": "toleration-key-01",
                    "Value": "toleration_val_01"
                }
            ]
        },
        "HighAvailability": true,
        "KerberosCluster": "emr-h6mtwtgn",
        "Namespace": "251233703-emr-a2jqs6n3",
        "PersistentVolume": {
            "CBSVolumes": [],
            "CFSVolumes": [],
            "COSVolumes": [],
            "StorageVolumeDetail": [],
            "StorageVolumeName": [],
            "VolumeMounts": []
        },
        "RayClusterId": 28,
        "RayClusterName": "raycluster",
        "RayClusterYaml": "apiVersion: ray.io/v1\nkind: RayCluster\nmetadata:\n    name: raycluster\n    namespace: 251233703-emr-a2jqs6n3\n    annotations:\n        ray.io/ft-enabled: \"true\"\n        runtime.emr.tencent.com/raycluster-managedby-emr: \"true\"\nspec:\n    headGroupSpec:\n        serviceType: ClusterIP\n        rayStartParams:\n            enable-head-ha: \"true\"\n            resources: '{\\\"Custom1\\\":1,\\\"Custom2\\\":5}'\n        template:\n            metadata:\n                labels:\n                    label-key-01: label-val-01\n            spec:\n                tolerations:\n                    - key: toleration-key-01\n                      value: toleration_val_01\n                nodeSelector:\n                    kubernetes.io/hostname: 10.0.1.61\n                containers:\n                    - name: ray-head\n                      image: ccr.ccs.tencentyun.com/emr-image-base/ray:2.52.0-65-653-dev\n                      resources:\n                        requests:\n                            cpu: \"1\"\n                            memory: 2G\n                        limits:\n                            cpu: \"1\"\n                            memory: 2G\n                      env:\n                        - name: testkey\n                          value: testval\n                      securityContext:\n                        capabilities:\n                            add:\n                                - SYS_ADMIN\n        replicas: 2\n    workerGroupSpecs:\n        - groupName: workerGroup0\n          replicas: 1\n          minReplicas: 1\n          maxReplicas: 1\n          rayStartParams: {}\n          template:\n            metadata: {}\n            spec:\n                containers:\n                    - name: ray-worker\n                      image: ccr.ccs.tencentyun.com/emr-image-base/ray:2.52.0-65-653-dev\n                      resources:\n                        requests:\n                            cpu: \"1\"\n                            memory: 2G\n                        limits:\n                            cpu: \"1\"\n                            memory: 2G\n                      securityContext:\n                        capabilities:\n                            add:\n                                - SYS_ADMIN\n        - groupName: WorkerGroup1\n          replicas: 1\n          minReplicas: 1\n          maxReplicas: 1\n          rayStartParams: {}\n          template:\n            metadata: {}\n            spec:\n                containers:\n                    - name: ray-worker\n                      image: ccr.ccs.tencentyun.com/emr-image-base/ray:2.52.0-65-653-dev\n                      resources:\n                        requests:\n                            cpu: \"1\"\n                            memory: 2G\n                        limits:\n                            cpu: \"1\"\n                            memory: 2G\n                      securityContext:\n                        capabilities:\n                            add:\n                                - SYS_ADMIN\n",
        "RedisInstance": {
            "Host": "10.0.1.120",
            "Id": "crs-2yrj6b29",
            "Port": 6379
        },
        "RequestId": "f79d7d08-51b4-4569-bd47-0a6cd2abed6a",
        "StorageConfigEnabled": false,
        "SubmitType": 1,
        "SupportExternalKerberosService": true,
        "Token": "emr-token-1pqyhv6r-n4fnvseb-9b6svpe3",
        "TotalPodCount": 4,
        "UpdateTime": "2025-12-29 11:27:53",
        "WorkerGroupSpecs": [
            {
                "Cpu": 1,
                "Gpu": 0,
                "GpuType": "",
                "GroupType": "WorkerGroup",
                "MaxNodes": 1,
                "MemSize": 2,
                "MinNodes": 1,
                "Name": "workerGroup0",
                "PersistentVolume": {
                    "CBSVolumes": [],
                    "CFSVolumes": [],
                    "COSVolumes": [],
                    "StorageVolumeDetail": [],
                    "StorageVolumeName": [],
                    "VolumeMounts": []
                },
                "PodCount": 1,
                "ResourceLabels": "null",
                "Scheduler": "",
                "StorageConfigEnabled": false
            },
            {
                "Cpu": 1,
                "Gpu": 0,
                "GpuType": "",
                "GroupType": "WorkerGroup",
                "MaxNodes": 1,
                "MemSize": 2,
                "MinNodes": 1,
                "Name": "WorkerGroup1",
                "PersistentVolume": {
                    "CBSVolumes": [],
                    "CFSVolumes": [],
                    "COSVolumes": [],
                    "StorageVolumeDetail": [],
                    "StorageVolumeName": [],
                    "VolumeMounts": []
                },
                "PodCount": 1,
                "ResourceLabels": "null",
                "Scheduler": "",
                "StorageConfigEnabled": false
            }
        ]
    }
}
```

