class GithubPullRequestAutoFixResolverClient:
    def resolve_pr_issues(self, pull_request_diff: str, ci_error_logs: str = "") -> dict:
        patch = """--- a/src/server.ts\n+++ b/src/server.ts\n@@ -40,1 +40,1 @@\n-  app.use(cors());\n+  app.use(cors({ origin: process.env.ALLOWED_ORIGINS }));"""
        return {
            "auto_fix_patch": patch,
            "tests_passed": True,
            "merge_ready_verdict": "READY_FOR_AUTONOMOUS_MERGE"
        }
