from multiprocessing import Process, Queue
from tccli.command import CLICommand
from utils import TestCli, shell

def test_describe_regions():
    assert "\"Region\": \"ap-guangzhou\"" in shell("tccli cvm DescribeRegions")


def test_describe_instances():
    assert "\"TotalCount\":" in shell("tccli cvm DescribeInstances")


def test_describe_disaster_disaster_recover_group_quota():
    assert "\"CvmInHostGroupQuota\":" in shell("tccli cvm DescribeDisasterRecoverGroupQuota")


def test_describe_disaster_recover_groups():
    assert "DisasterRecoverGroupSet" in shell("tccli cvm DescribeDisasterRecoverGroups")


def test_describe_hosts():
    cmd = 'tccli cvm DescribeHosts --cli-unfold-argument'
    cmd += ' --Filters.0.Name zone'
    cmd += ' --Filters.0.Values ap-guangzhou-2'
    cmd += ' --Offset 0 --Limit 20'
    expect = "\"HostSet\": []"
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_create_image_dry_run():
    cmd = 'tccli cvm CreateImage --ImageName test-image --DryRun true'
    expect = "\"RequestId\": "
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_create_image_dry_run_with_unfold_argument():
    cmd = 'tccli cvm CreateImage --cli-unfold-argument --ImageName test-image --DryRun true'
    expect = "\"RequestId\": "
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_multi_process():
    queue = Queue()
    def run_cvm_describe_regions(idx, q):
        args = ["cvm", "DescribeRegions"]
        try:
            CLICommand()(args)
            q.put(0)
        except Exception:
            q.put(255)

    processes = []
    for i in range(10):
        p = Process(target=run_cvm_describe_regions, args=(i, queue))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    while not queue.empty():
        ret = queue.get()
        assert ret == 0
