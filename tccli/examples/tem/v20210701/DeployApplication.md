**Example 1: 应用部署**

应用部署

Input: 

```
tccli tem DeployApplication --cli-unfold-argument  \
    --ApplicationId app-5vaz8x85 \
    --ConfEdited False \
    --DeployMode JAR \
    --JdkVersion KONA:11 \
    --PkgName tem/pkg/130xxxx/app-5vaz8x85/1733xxxx/K8sDemo-1.0.jar \
    --SpeedUp True \
    --OsFlavour ALPINE \
    --DeployVersion 20241202165113 \
    --JvmOpts -Xms128m -XX:MetaspaceSize=128m \
    --InitPodNum 3 \
    --CpuSpec 1 \
    --MemorySpec 2 \
    --EnvConf.0.Key key \
    --EnvConf.0.Value val \
    --EnvConf.0.Type default \
    --EnvConf.0.Config  \
    --EnvConf.0.Secret  \
    --LogEnable 0 \
    --SecurityGroupIds sg-1zwhplpi \
    --EnvironmentId en-dpxydze5 \
    --Service.ServicePortMappingList.0.Type CLUSTER \
    --Service.ServicePortMappingList.0.ServiceName k8s-svc-test \
    --Service.ServicePortMappingList.0.ClusterIp 172.16.56.122 \
    --Service.ServicePortMappingList.0.ExternalIp 10.xx.xx.xx \
    --Service.ServicePortMappingList.0.ExternalDomain ext.domain.com \
    --Service.ServicePortMappingList.0.SubnetId subnet-xxx \
    --Service.ServicePortMappingList.0.VpcId vpc-oxyzq5xx \
    --Service.ServicePortMappingList.0.LoadBalanceId 10.xx.xx.xx \
    --Service.ServicePortMappingList.0.Yaml apiVersion: xxxxx \
    --Service.ServicePortMappingList.0.Ports 8080 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Port 8080 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.TargetPort 8080 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Protocol TCP \
    --Service.EnableRegistryNextDeploy 0 \
    --Service.FlushAll True \
    --UseRegistryDefaultConfig False \
    --EnableTracing 0 \
    --SettingConfs.0.ConfigDataName cfg-test-1 \
    --SettingConfs.0.MountedPath /data \
    --SettingConfs.0.SecretDataName secret-name \
    --DeployStrategyConf.TotalBatchCount 1 \
    --DeployStrategyConf.BetaBatchNum 0 \
    --DeployStrategyConf.DeployStrategyType 3 \
    --DeployStrategyConf.MinAvailable 1 \
    --DeployStrategyConf.Force True \
    --DeployStrategyConf.BatchInterval 0 \
    --PostStart /bin/sh
-c
curl localhost:8080/postStart \
    --PreStop /bin/sh
-c
wget --server-response --spider -S --no-verbose --header="Content-Type:application/json" --post-data='{"serverName":"api-basic"}' "http://localhost:9900/actuator/stopmsg"
sleep 30s
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

