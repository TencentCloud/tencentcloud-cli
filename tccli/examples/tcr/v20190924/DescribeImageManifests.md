**Example 1: 查询容器镜像Manifest信息**

查询容器镜像Manifest、Config和Labels信息

Input: 

```
tccli tcr DescribeImageManifests --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --NamespaceName hbd \
    --RepositoryName repo1 \
    --ImageVersion 1
```

Output: 
```
{
    "Response": {
        "Config": "\"{\\\"architecture\\\":\\\"amd64\\\",\\\"config\\\":{\\\"Env\\\":[\\\"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\\\"],\\\"Cmd\\\":[\\\"registry\\\",\\\"serve\\\",\\\"-c\\\",\\\"/etc/registry/config.yaml\\\"],\\\"WorkingDir\\\":\\\"/etc/registry\\\",\\\"Labels\\\":{\\\"org.opencontainers.image.ref.name\\\":\\\"ubuntu\\\",\\\"org.opencontainers.image.version\\\":\\\"18.04\\\"},\\\"ArgsEscaped\\\":true,\\\"OnBuild\\\":null},\\\"created\\\":\\\"2024-07-16T03:10:41.813066079Z\\\",\\\"history\\\":[{\\\"created\\\":\\\"2023-05-30T09:32:07.458866408Z\\\",\\\"created_by\\\":\\\"/bin/sh -c #(nop)  ARG RELEASE\\\",\\\"empty_layer\\\":true},{\\\"created\\\":\\\"2023-05-30T09:32:07.512060632Z\\\",\\\"created_by\\\":\\\"/bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH\\\",\\\"empty_layer\\\":true},{\\\"created\\\":\\\"2023-05-30T09:32:07.566627883Z\\\",\\\"created_by\\\":\\\"/bin/sh -c #(nop)  LABEL org.opencontainers.image.ref.name=ubuntu\\\",\\\"empty_layer\\\":true},{\\\"created\\\":\\\"2023-05-30T09:32:07.623484379Z\\\",\\\"created_by\\\":\\\"/bin/sh -c #(nop)  LABEL org.opencontainers.image.version=18.04\\\",\\\"empty_layer\\\":true},{\\\"created\\\":\\\"2023-05-30T09:32:09.125568601Z\\\",\\\"created_by\\\":\\\"/bin/sh -c #(nop) ADD file:3c74e7e08cbf9a87694ce6fa541af617599680fa54d9e48556fc0fbc120b4a83 in / \\\"},{\\\"created\\\":\\\"2023-05-30T09:32:09.432301537Z\\\",\\\"created_by\\\":\\\"/bin/sh -c #(nop)  CMD [\\\\\\\"/bin/bash\\\\\\\"]\\\",\\\"empty_layer\\\":true},{\\\"created\\\":\\\"2024-07-10T10:00:15.101428263Z\\\",\\\"created_by\\\":\\\"WORKDIR /etc/registry\\\",\\\"comment\\\":\\\"buildkit.dockerfile.v0\\\"},{\\\"created\\\":\\\"2024-07-10T10:00:15.131434138Z\\\",\\\"created_by\\\":\\\"ADD nsswitch.conf /etc/ # buildkit\\\",\\\"comment\\\":\\\"buildkit.dockerfile.v0\\\"},{\\\"created\\\":\\\"2024-07-16T03:10:41.478957062Z\\\",\\\"created_by\\\":\\\"COPY _output/bin/registry /usr/bin/registry # buildkit\\\",\\\"comment\\\":\\\"buildkit.dockerfile.v0\\\"},{\\\"created\\\":\\\"2024-07-16T03:10:41.813066079Z\\\",\\\"created_by\\\":\\\"RUN /bin/sh -c chmod +x /usr/bin/registry # buildkit\\\",\\\"comment\\\":\\\"buildkit.dockerfile.v0\\\"},{\\\"created\\\":\\\"2024-07-16T03:10:41.813066079Z\\\",\\\"created_by\\\":\\\"CMD [\\\\\\\"registry\\\\\\\" \\\\\\\"serve\\\\\\\" \\\\\\\"-c\\\\\\\" \\\\\\\"/etc/registry/config.yaml\\\\\\\"]\\\",\\\"comment\\\":\\\"buildkit.dockerfile.v0\\\",\\\"empty_layer\\\":true}],\\\"os\\\":\\\"linux\\\",\\\"rootfs\\\":{\\\"type\\\":\\\"layers\\\",\\\"diff_ids\\\":[\\\"sha256:548a79621a426b4eb077c926eabac5a8620c454fb230640253e1b44dc7dd7562\\\",\\\"sha256:b13470a221901678d27505896239cc4a089d92aa9a62140eeb217ff5fa44f5ae\\\",\\\"sha256:30727457001005d34b6b00e8b4499d9f967a1bf302e6159e4e08a7f3651839e4\\\",\\\"sha256:cf8534d7e603a2e8826d0021023fb76200f205d56e1e993fd3529323437eab9a\\\",\\\"sha256:cf8534d7e603a2e8826d0021023fb76200f205d56e1e993fd3529323437eab9a\\\"]}}\"",
        "Manifest": "{\"config\":{\"digest\":\"sha256:17382a17d531887484413bd5177282452cece7a1c21910eb9b273c56db74abd3\",\"mediaType\":\"application/vnd.docker.container.image.v1+json\",\"size\":2333},\"layers\":[{\"digest\":\"sha256:41af1b5f0f51947706ae712999cf098bef968a7799e7cb4bb2268829e62a6ab3\",\"mediaType\":\"application/vnd.docker.image.rootfs.diff.tar.gzip\",\"size\":26717357},{\"digest\":\"sha256:694d0c491cdb576620f5cdff056869e9c14763cf386e2d420e6703e240bed23e\",\"mediaType\":\"application/vnd.docker.image.rootfs.diff.tar.gzip\",\"size\":117},{\"digest\":\"sha256:7661ef468d87d6f1f140e61d0d288742552c417339d3b00edd78476c877ceaf9\",\"mediaType\":\"application/vnd.docker.image.rootfs.diff.tar.gzip\",\"size\":169},{\"digest\":\"sha256:0ce6b312368cc6cc47045e00978809e6d3aeff30108e1bd05a6fcb6f54aaeee7\",\"mediaType\":\"application/vnd.docker.image.rootfs.diff.tar.gzip\",\"size\":6358509},{\"digest\":\"sha256:0ce6b312368cc6cc47045e00978809e6d3aeff30108e1bd05a6fcb6f54aaeee7\",\"mediaType\":\"application/vnd.docker.image.rootfs.diff.tar.gzip\",\"size\":6358509}],\"mediaType\":\"application/vnd.docker.distribution.manifest.v2+json\",\"schemaVersion\":2}",
        "RequestId": "c6188203-d7fd-4760-8b16-f9f41396fa86",
        "Size": 39436994
    }
}
```

