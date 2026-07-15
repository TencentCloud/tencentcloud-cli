**Example 1: 修改智能体实例的参数列表**



Input: 

```
tccli tdai ModifyAgentInstanceParameters --cli-unfold-argument  \
    --InstanceId agentins-551mli9x \
    --SqlAgentParameter.InstanceInfos.0.Region ap-chengdu \
    --SqlAgentParameter.InstanceInfos.0.InstanceId cdb-jgmilzl8 \
    --SqlAgentParameter.InstanceInfos.0.DatabaseName  \
    --SqlAgentParameter.InstanceInfos.0.TableName  \
    --SqlAgentParameter.CodeRepo.RepoUrl git@git.woa.com:calvinliao/test-sql-agent.git \
    --SqlAgentParameter.CodeRepo.Branch master \
    --SqlAgentParameter.CodeRepo.GitCommitPipelines bdbe54afaa7e60b11cd87682bd9ab59c92a489ac \
    --SqlAgentParameter.CodeRepo.GitORMType goframe
```

Output: 
```
{
    "Response": {
        "RequestId": "a070f1a2-7538-5318-c843-6b47607aa78c"
    }
}
```

