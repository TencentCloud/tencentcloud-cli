**Example 1: 增量修改模型服务**



Input: 

```
tccli tione ModifyModelServicePartialConfig --cli-unfold-argument  \
    --ServiceId ms-kxqfprc5-1 \
    --ServiceLimit.EnableInstanceRpsLimit True \
    --ServiceLimit.InstanceRpsLimit 22
```

Output: 
```
{
    "Response": {
        "Service": {
            "ServiceGroupId": "ms-kxqfprc5",
            "ServiceId": "ms-kxqfprc5-1",
            "ServiceGroupName": "test-ls-onnx-fp16",
            "ServiceDescription": "",
            "ServiceInfo": {
                "Replicas": 1,
                "ImageInfo": {
                    "ImageType": "PRE_SET",
                    "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu:py38-torch1.9.0-onnx1.11.1-cu111-2.0.1",
                    "RegistryRegion": "",
                    "RegistryId": ""
                },
                "Env": [],
                "Resources": {
                    "Cpu": 32000,
                    "Memory": 131072,
                    "Gpu": 100,
                    "RealGpu": 100,
                    "GpuType": "T4",
                    "RealGpuDetailSet": [
                        {
                            "Name": "T4",
                            "Value": 100
                        }
                    ]
                },
                "InstanceType": "TI.GN7.8XLARGE128.POST",
                "ModelInfo": {
                    "ModelId": "m-549834620985377536",
                    "ModelName": "test-ls-onnx",
                    "ModelVersionId": "mv-v1-549853865408430848",
                    "ModelVersion": "v1o2",
                    "ModelSource": "COS",
                    "ModelType": "ACCELERATE",
                    "CosPathInfo": {
                        "Bucket": "ls-gz-1256580188",
                        "Region": "ap-guangzhou",
                        "Paths": [
                            "优化模型/m-549834620985377536/mv-v1-549853865408430848/"
                        ],
                        "Uin": "100005348929",
                        "SubUin": "100023251204"
                    },
                    "GpuType": "T4",
                    "AlgorithmFramework": ""
                },
                "VolumeMount": null,
                "LogEnable": false,
                "LogConfig": null,
                "AuthorizationEnable": false,
                "ScaleMode": "MANUAL",
                "HorizontalPodAutoscaler": null,
                "CronScaleJobs": [],
                "ScaleStrategy": "",
                "ScheduledAction": {
                    "ScheduleStop": true,
                    "ScheduleStopTime": "2022-11-28T03:59:12Z"
                },
                "Status": {
                    "Replicas": 1,
                    "UpdatedReplicas": 1,
                    "ReadyReplicas": 1,
                    "AvailableReplicas": 1,
                    "UnavailableReplicas": 0,
                    "Status": "Normal",
                    "Reason": "",
                    "Conditions": [
                        {
                            "Message": "Deployment has minimum availability.",
                            "Reason": "MinimumReplicasAvailable",
                            "Status": "True",
                            "Type": "Available",
                            "LastTransitionTime": "2022-11-28T11:03:18+08:00",
                            "LastUpdateTime": "2022-11-28T11:03:18+08:00"
                        },
                        {
                            "Message": "ReplicaSet \"ms-kxqfprc5-1-5b4fdfd87c\" has successfully progressed.",
                            "Reason": "NewReplicaSetAvailable",
                            "Status": "True",
                            "Type": "Progressing",
                            "LastTransitionTime": "2022-06-17T15:42:29+08:00",
                            "LastUpdateTime": "2022-11-28T11:03:18+08:00"
                        }
                    ]
                },
                "Weight": 0,
                "PodList": [
                    "{\"metadata\":{\"name\":\"ms-kxqfprc5-1-5b4fdfd87c-kstbw\",\"generateName\":\"ms-kxqfprc5-1-5b4fdfd87c-\",\"namespace\":\"infer-100005348929\",\"selfLink\":\"/api/v1/namespaces/infer-100005348929/pods/ms-kxqfprc5-1-5b4fdfd87c-kstbw\",\"uid\":\"ddeacfdd-e991-4fe4-963b-427d9e5e7691\",\"resourceVersion\":\"8798003156\",\"creationTimestamp\":\"2022-11-28T02:59:44Z\",\"labels\":{\"app\":\"ms-kxqfprc5-1\",\"appid\":\"1256580188\",\"owner\":\"tiems\",\"pod-template-hash\":\"5b4fdfd87c\",\"resource-remark/real-gpu\":\"100\",\"service-group-id\":\"ms-kxqfprc5\",\"service-id\":\"ms-kxqfprc5-1\",\"subuin\":\"100023251204\",\"ti.cloud.tencent.com/cls-region\":\"ap-guangzhou\",\"ti.cloud.tencent.com/gpu-type\":\"T4\",\"ti.cloud.tencent.com/internet-access\":\"true\",\"ti.cloud.tencent.com/prefer-eks\":\"true\",\"ti.cloud.tencent.com/task-type\":\"Inference\",\"ti.cloud.tencent.com/user-id\":\"100005348929\",\"uin\":\"100005348929\"},\"annotations\":{\"eks.tke.cloud.tencent.com/cluster-ip-switch\":\"cluster\",\"eks.tke.cloud.tencent.com/gpu-type\":\"T4\",\"eks.tke.cloud.tencent.com/image-gc-high-threshold\":\"95\",\"eks.tke.cloud.tencent.com/image-gc-low-threshold\":\"90\",\"eks.tke.cloud.tencent.com/recreate-node-lost-pod\":\"false\",\"eks.tke.cloud.tencent.com/reserve-sandbox-duration\":\"1m\",\"eks.tke.cloud.tencent.com/reserve-succeeded-sandbox\":\"true\",\"eks.tke.cloud.tencent.com/root-cbs-size\":\"50\",\"eks.tke.cloud.tencent.com/security-group-id\":\"sg-4jqc93cx\",\"eks.tke.cloud.tencent.com/use-image-cache\":\"imc-s1qe3dxi\",\"image-infos\":\"{\\\"ImageType\\\":\\\"PRE_SET\\\",\\\"ImageUrl\\\":\\\"tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu:py38-torch1.9.0-onnx1.11.1-cu111-2.0.1\\\"}\",\"model-infos\":\"{\\\"ModelId\\\":\\\"m-549834620985377536\\\",\\\"ModelName\\\":\\\"test-ls-onnx\\\",\\\"ModelVersionId\\\":\\\"mv-v1-549853865408430848\\\",\\\"ModelVersion\\\":\\\"v1o2\\\",\\\"ModelSource\\\":\\\"COS\\\",\\\"ModelType\\\":\\\"ACCELERATE\\\",\\\"CosPathInfo\\\":{\\\"Bucket\\\":\\\"ls-gz-1256580188\\\",\\\"Region\\\":\\\"ap-guangzhou\\\",\\\"Paths\\\":[\\\"优化模型/m-549834620985377536/mv-v1-549853865408430848/\\\"],\\\"Uin\\\":\\\"100005348929\\\",\\\"SubUin\\\":\\\"100023251204\\\"},\\\"GpuType\\\":\\\"T4\\\"}\",\"scheduling.k8s.io/group-auto-create\":\"true\",\"scheduling.k8s.io/group-name\":\"podgroup-ddeacfdd-e991-4fe4-963b-427d9e5e7691\",\"ti.cloud.tencent.com/cls-enable\":\"false\",\"ti.cloud.tencent.com/cls-region\":\"ap-guangzhou\",\"ti.cloud.tencent.com/gpu-type\":\"T4\",\"ti.cloud.tencent.com/instance-type\":\"TI.GN7.8XLARGE128.POST\",\"ti.cloud.tencent.com/internet-access\":\"true\",\"ti.cloud.tencent.com/prefer-eks\":\"true\",\"ti.cloud.tencent.com/resourcegroup-id\":\"\",\"ti.cloud.tencent.com/task-type\":\"Inference\",\"ti.cloud.tencent.com/user-id\":\"100005348929\",\"ti.ems/gpu-type\":\"T4\",\"ti.ems/service-start-time\":\"2022-11-28T10:59:44+08:00\",\"tke.cloud.tencent.com/pod-type\":\"eklet\"},\"ownerReferences\":[{\"apiVersion\":\"apps/v1\",\"kind\":\"ReplicaSet\",\"name\":\"ms-kxqfprc5-1-5b4fdfd87c\",\"uid\":\"8227cbe7-0910-4dd0-9f4d-13e3be3fc031\",\"controller\":true,\"blockOwnerDeletion\":true}],\"finalizers\":[\"ti.ems/billing\"]},\"spec\":{\"volumes\":[{\"name\":\"model\",\"emptyDir\":{\"sizeLimit\":\"100Gi\"}},{\"name\":\"sidecar-conf-volume\",\"configMap\":{\"name\":\"ms-kxqfprc5-1-cm\",\"items\":[{\"key\":\"NGINX_CONF\",\"path\":\"nginx.conf\"}],\"defaultMode\":420}},{\"name\":\"default-token-7bfhp\",\"secret\":{\"secretName\":\"default-token-7bfhp\",\"defaultMode\":420}},{\"name\":\"algo-auth\",\"emptyDir\":{}}],\"initContainers\":[{\"name\":\"init\",\"image\":\"tione.tencentcloudcr.com/qcloud-ti-platform/coscli-download:1.0\",\"env\":[{\"name\":\"QCLOUD_CONTAINER_INSTANCE_CREDENTIALS_URL\",\"valueFrom\":{\"secretKeyRef\":{\"name\":\"subuin-100010074434-cos-download-token\",\"key\":\"token\"}}},{\"name\":\"BUCKET\",\"value\":\"ls-gz-1256580188\"},{\"name\":\"ENDPOINT\",\"value\":\"cos.ap-guangzhou.myqcloud.com\"},{\"name\":\"REMOTE_PATH\",\"value\":\"优化模型/m-549834620985377536/mv-v1-549853865408430848/\"},{\"name\":\"LOCAL_PATH\",\"value\":\"/data/model\"},{\"name\":\"NODE_IP\",\"valueFrom\":{\"fieldRef\":{\"apiVersion\":\"v1\",\"fieldPath\":\"status.hostIP\"}}},{\"name\":\"POD_NAME\",\"valueFrom\":{\"fieldRef\":{\"apiVersion\":\"v1\",\"fieldPath\":\"metadata.name\"}}},{\"name\":\"POD_TEMPLATE_HASH\",\"valueFrom\":{\"fieldRef\":{\"apiVersion\":\"v1\",\"fieldPath\":\"metadata.labels['pod-template-hash']\"}}},{\"name\":\"TI_SERVICE_ID\",\"valueFrom\":{\"fieldRef\":{\"apiVersion\":\"v1\",\"fieldPath\":\"metadata.labels['service-id']\"}}}],\"resources\":{\"limits\":{\"cpu\":\"1\",\"memory\":\"512Mi\"},\"requests\":{\"cpu\":\"1\",\"memory\":\"512Mi\"}},\"volumeMounts\":[{\"name\":\"model\",\"mountPath\":\"/data/model\",\"subPathExpr\":\"$(TI_SERVICE_ID)-$(POD_TEMPLATE_HASH)\"},{\"name\":\"default-token-7bfhp\",\"readOnly\":true,\"mountPath\":\"/var/run/secrets/kubernetes.io/serviceaccount\"}],\"terminationMessagePath\":\"/dev/termination-log\",\"terminationMessagePolicy\":\"File\",\"imagePullPolicy\":\"Always\"}],\"containers\":[{\"name\":\"main\",\"image\":\"tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu:py38-torch1.9.0-onnx1.11.1-cu111-2.0.1\",\"ports\":[{\"name\":\"http-metrics\",\"containerPort\":9100,\"protocol\":\"TCP\"}],\"env\":[{\"name\":\"NODE_IP\",\"valueFrom\":{\"fieldRef\":{\"apiVersion\":\"v1\",\"fieldPath\":\"status.hostIP\"}}},{\"name\":\"POD_NAME\",\"valueFrom\":{\"fieldRef\":{\"apiVersion\":\"v1\",\"fieldPath\":\"metadata.name\"}}},{\"name\":\"POD_TEMPLATE_HASH\",\"valueFrom\":{\"fieldRef\":{\"apiVersion\":\"v1\",\"fieldPath\":\"metadata.labels['pod-template-hash']\"}}},{\"name\":\"TI_SERVICE_ID\",\"valueFrom\":{\"fieldRef\":{\"apiVersion\":\"v1\",\"fieldPath\":\"metadata.labels['service-id']\"}}}],\"resources\":{\"limits\":{\"cpu\":\"32\",\"memory\":\"128Gi\",\"nvidia.com/gpu\":\"1\",\"tke.cloud.tencent.com/eni-ip\":\"1\"},\"requests\":{\"cpu\":\"31200m\",\"memory\":\"97977Mi\",\"nvidia.com/gpu\":\"1\",\"tke.cloud.tencent.com/eni-ip\":\"1\"}},\"volumeMounts\":[{\"name\":\"model\",\"mountPath\":\"/data/model\",\"subPathExpr\":\"$(TI_SERVICE_ID)-$(POD_TEMPLATE_HASH)\"},{\"name\":\"default-token-7bfhp\",\"readOnly\":true,\"mountPath\":\"/var/run/secrets/kubernetes.io/serviceaccount\"},{\"name\":\"algo-auth\",\"readOnly\":true,\"mountPath\":\"/var/run/ti/.train.lock\"}],\"readinessProbe\":{\"tcpSocket\":{\"port\":8501},\"initialDelaySeconds\":5,\"timeoutSeconds\":1,\"periodSeconds\":5,\"successThreshold\":1,\"failureThreshold\":3},\"terminationMessagePath\":\"/dev/termination-log\",\"terminationMessagePolicy\":\"File\",\"imagePullPolicy\":\"Always\"}],\"restartPolicy\":\"Always\",\"terminationGracePeriodSeconds\":30,\"dnsPolicy\":\"ClusterFirst\",\"serviceAccountName\":\"default\",\"serviceAccount\":\"default\",\"automountServiceAccountToken\":false,\"nodeName\":\"eklet-subnet-4d7xupy2\",\"securityContext\":{},\"imagePullSecrets\":[{\"name\":\"system-image-access-secret\"},{\"name\":\"system-image-access-secret\"}],\"schedulerName\":\"volcano\",\"tolerations\":[{\"key\":\"node.kubernetes.io/not-ready\",\"operator\":\"Exists\",\"effect\":\"NoExecute\",\"tolerationSeconds\":300},{\"key\":\"node.kubernetes.io/unreachable\",\"operator\":\"Exists\",\"effect\":\"NoExecute\",\"tolerationSeconds\":300},{\"key\":\"eks.tke.cloud.tencent.com/eklet\",\"effect\":\"NoSchedule\"}],\"priority\":0,\"readinessGates\":[{\"conditionType\":\"cloud.tencent.com/load-balancer-backendgroup-ready\"}],\"enableServiceLinks\":false,\"preemptionPolicy\":\"PreemptLowerPriority\"},\"status\":{\"phase\":\"Running\",\"conditions\":[{\"type\":\"cloud.tencent.com/load-balancer-backendgroup-ready\",\"status\":\"True\",\"lastProbeTime\":null,\"lastTransitionTime\":\"2022-11-28T03:03:18Z\",\"reason\":\"LoadBalancerNetworkGroupReady\",\"message\":\"Marking condition \\\"cloud.tencent.com/load-balancer-backendgroup-ready\\\" to True.\"},{\"type\":\"ReportMonitor\",\"status\":\"True\",\"lastProbeTime\":null,\"lastTransitionTime\":\"2022-11-28T03:00:15Z\"},{\"type\":\"Initialized\",\"status\":\"True\",\"lastProbeTime\":null,\"lastTransitionTime\":\"2022-11-28T03:00:29Z\"},{\"type\":\"Ready\",\"status\":\"True\",\"lastProbeTime\":null,\"lastTransitionTime\":\"2022-11-28T03:03:18Z\"},{\"type\":\"ContainersReady\",\"status\":\"True\",\"lastProbeTime\":null,\"lastTransitionTime\":\"2022-11-28T03:03:00Z\"},{\"type\":\"PodScheduled\",\"status\":\"True\",\"lastProbeTime\":null,\"lastTransitionTime\":\"2022-11-28T02:59:45Z\"}],\"hostIP\":\"9.0.99.153\",\"podIP\":\"9.0.99.153\",\"podIPs\":[{\"ip\":\"9.0.99.153\"}],\"startTime\":\"2022-11-28T03:00:15Z\",\"initContainerStatuses\":[{\"name\":\"init\",\"state\":{\"terminated\":{\"exitCode\":0,\"reason\":\"Completed\",\"startedAt\":\"2022-11-28T03:00:25Z\",\"finishedAt\":\"2022-11-28T03:00:29Z\",\"containerID\":\"containerd://969c3520c248d04a2ecb578c80c4274bfe638bb0140afc89425a73ebb0b4b405\"}},\"lastState\":{},\"ready\":true,\"restartCount\":0,\"image\":\"tione.tencentcloudcr.com/qcloud-ti-platform/coscli-download:1.0\",\"imageID\":\"tione.tencentcloudcr.com/qcloud-ti-platform/coscli-download@sha256:a6b6291af1ba505734fdf3958898817b682bbdfd7d5d7e7059c58e4ea3686b9a\",\"containerID\":\"containerd://969c3520c248d04a2ecb578c80c4274bfe638bb0140afc89425a73ebb0b4b405\"}],\"containerStatuses\":[{\"name\":\"main\",\"state\":{\"running\":{\"startedAt\":\"2022-11-28T03:00:59Z\"}},\"lastState\":{},\"ready\":true,\"restartCount\":0,\"image\":\"tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu:py38-torch1.9.0-onnx1.11.1-cu111-2.0.1\",\"imageID\":\"tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu@sha256:fdf88adbf511c2f72e848348288a17ed0a1f25f9902efcbcbe5b18f57cde36b1\",\"containerID\":\"containerd://dabe26524627ee3d7792c5d6ccf41a656109809738da295fc1dd7998c61a246b\",\"started\":true},{\"name\":\"sidecar-nginx\",\"state\":{\"running\":{\"startedAt\":\"2022-11-28T03:01:05Z\"}},\"lastState\":{},\"ready\":true,\"restartCount\":0,\"image\":\"tione.tencentcloudcr.com/qcloud-ti-platform/openresty:1.30\",\"imageID\":\"tione.tencentcloudcr.com/qcloud-ti-platform/openresty@sha256:9b6181327e8114013e0ca1cfe4c74819533caa9027cd0057f87bf433089fb22d\",\"containerID\":\"containerd://3250a013c8a48627126cd046d72b3fdfc5adff22464af835ff059e1924b87ad2\",\"started\":true}],\"qosClass\":\"Burstable\"}}\n"
                ],
                "ResourceTotal": {
                    "Cpu": 32000,
                    "Memory": 131072,
                    "Gpu": 100,
                    "RealGpu": 100,
                    "GpuType": "T4",
                    "RealGpuDetailSet": [
                        {
                            "Name": "T4",
                            "Value": 100
                        }
                    ]
                },
                "OldReplicas": 1,
                "HybridBillingPrepaidReplicas": 0,
                "OldHybridBillingPrepaidReplicas": 0,
                "ServiceLimit": {
                    "EnableInstanceRpsLimit": true,
                    "InstanceRpsLimit": 22
                },
                "BillingStatus": "BILLING",
                "BillingUnits": [
                    {
                        "Spec": "TI.GN7.8XLARGE128.POST",
                        "Count": 1
                    }
                ],
                "ModelHotUpdateEnable": false
            },
            "ClusterId": "",
            "Region": "ap-guangzhou",
            "Namespace": "infer-100005348929",
            "ChargeType": "POSTPAID_BY_HOUR",
            "ResourceGroupId": "",
            "IngressName": "user-ingress",
            "CreatedBy": "100023251204",
            "CreateTime": "2022-06-17T07:42:19Z",
            "UpdateTime": "2022-11-28T02:59:43Z",
            "Uin": "100005348929",
            "SubUin": "",
            "AppId": 0,
            "BusinessStatus": "CREATE_SUCCEED",
            "CreateFailedReason": "CREATE_SUCCEED",
            "Status": "Normal",
            "BillingInfo": "",
            "Weight": 100,
            "CreateSource": "",
            "Version": "1",
            "LatestVersion": "",
            "ServiceLimit": null,
            "ScheduledAction": null
        },
        "RequestId": "6b73484d-aa38-40c4-a8c6-c3205dbbc9c0"
    }
}
```

