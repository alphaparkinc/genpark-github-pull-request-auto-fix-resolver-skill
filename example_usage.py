from client import GithubPullRequestAutoFixResolverClient

def main():
    client = GithubPullRequestAutoFixResolverClient()
    diff = "+ app.use(cors());"
    res = client.resolve_pr_issues(diff, "Security lint error: Wildcard CORS origin not allowed.")
    print(f"Verdict: {res['merge_ready_verdict']}")
    print(f"Tests Passed: {res['tests_passed']}")
    print("Auto-Fix Patch:")
    print(res["auto_fix_patch"])

if __name__ == "__main__":
    main()
