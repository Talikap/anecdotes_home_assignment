from api_utils import fetch_data

def collect_user_details(config, token):
    # Collect authenticated user details (E1).
    
    headers = {"Authorization": f"Bearer {token}"}
    user_url = config["base_url"] + config["user_details_endpoint"]
    user_details = fetch_data(user_url, headers)
    if user_details:
        print("E1: User Details Collected")
    else:
        print("E1: Failed to collect user details")
    return user_details


def collect_posts(config, limit=60):
    #Collect a list of posts (E2) with a specified limit.

    posts_url = f"{config['base_url']}{config['posts_endpoint']}"

    posts_data = fetch_data(posts_url, limit=limit)

    if posts_data and "posts" in posts_data:
        posts = posts_data.get("posts", [])
        print(f"E2: Collected {len(posts)} posts")
        return posts
    else:
        print("E2: Failed to collect posts")
        return []


def collect_posts_with_comments(config, posts):
    # Collect 60 posts with comments (E3).

    posts_with_comments = []
    for post in posts:
        comments_url = config["base_url"] + config["comments_endpoint"].format(post_id=post["id"])
        comments = fetch_data(comments_url)
        post["comments"] = comments.get("comments", [])
        posts_with_comments.append(post)
    print(f"E3: Collected {len(posts_with_comments)} posts with comments")
    return posts_with_comments


def collect_evidence(config, token):
    #Main function to collect all evidence.

    user_details = collect_user_details(config, token)
    posts = collect_posts(config)
    posts_with_comments = collect_posts_with_comments(config, posts)

    return {
        "user_details": user_details,
        "posts": posts,
        "posts_with_comments": posts_with_comments
    }
