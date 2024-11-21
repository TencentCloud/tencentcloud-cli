**Example 1: 应用部署**

应用部署

Input: 

```
tccli tem DeployApplication --cli-unfold-argument  \
    --ApplicationId app-5vaz8x85 \
    --ConfEdited False \
    --CpuSpec 1 \
    --DeployMode IMAGE \
    --DeployStrategyConf.BatchInterval 0 \
    --DeployStrategyConf.BetaBatchNum 0 \
    --DeployStrategyConf.DeployStrategyType 0 \
    --DeployStrategyConf.Force False \
    --DeployStrategyConf.MinAvailable 1 \
    --DeployStrategyConf.TotalBatchCount 1 \
    --DeployVersion hello-world \
    --EnableTracing 0 \
    --EnvironmentId en-dpxydze5 \
    --ImgRepo tem_demo/tem_demo \
    --InitPodNum 1 \
    --JvmOpts  \
    --LogEnable 0 \
    --MemorySpec 2 \
    --PostStart  \
    --PreStop  \
    --RepoServer ccr.ccs.tencentyun.com \
    --RepoType 4 \
    --SecurityGroupIds  \
    --Service.EnableRegistryNextDeploy 0 \
    --Service.FlushAll True \
    --Service.ServicePortMappingList.0.ClusterIp 172.16.207.15 \
    --Service.ServicePortMappingList.0.ExternalDomain  \
    --Service.ServicePortMappingList.0.ExternalIp  \
    --Service.ServicePortMappingList.0.LoadBalanceId  \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Port 8201 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Protocol TCP \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.TargetPort 8201 \
    --Service.ServicePortMappingList.0.Ports 8201 \
    --Service.ServicePortMappingList.0.ServiceName pk-test-clb-2 \
    --Service.ServicePortMappingList.0.SubnetId  \
    --Service.ServicePortMappingList.0.Type CLUSTER \
    --Service.ServicePortMappingList.0.VpcId  \
    --Service.ServicePortMappingList.0.Yaml apiVersion: v1
kind: Service
metadata:
  creationTimestamp: '2024-10-25T10:52:08Z'
  finalizers: []
  labels:
    tem-application-id: app-5vaz8x85
    tem-internal: 'false'
    tem-service: pk-test-clb-2
  managedFields:
  - apiVersion: v1
    fieldsType: FieldsV1
    fieldsV1: {}
    manager: okhttp
    operation: Update
    time: '2024-10-25T10:52:08Z'
  name: pk-test-clb-2
  namespace: default
  ownerReferences: []
  resourceVersion: '24527383012'
  selfLink: /api/v1/namespaces/default/services/pk-test-clb-2
  uid: 205ee301-8743-46ac-bc6f-d757eeab27bb
spec:
  type: ClusterIP
  clusterIP: 172.16.207.15
  clusterIPs:
  - 172.16.207.15
  externalIPs: []
  ipFamilies: []
  loadBalancerSourceRanges: []
  ports:
  - name: pk-test-clb-2-port-tcp-8201-8201
    port: 8201
    protocol: TCP
    targetPort:
      kind: 0
      intVal: 8201
  selector:
    tem-service: app0925
  sessionAffinity: None
  topologyKeys: []
status:
  conditions: []
  loadBalancer:
    ingress: []
 \
    --TcrInstanceId tcr-cwnk7hmb \
    --UseRegistryDefaultConfig False
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": "revision-xxxxxx"
    }
}
```

