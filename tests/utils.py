import os


class TestCli(object):

    def run_cmd(self, cmd):
        result = os.popen(cmd)
        return result

    def equal(self, cmd, expect):
        run = self.run_cmd(cmd)
        result = run.read()
        # self.assertEqual(result, expect, "Unexpected Result")
        assert result.find(expect) >= 0
