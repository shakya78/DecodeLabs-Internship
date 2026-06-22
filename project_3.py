# AI Recommendation System - DecodeLabs Project 3

print("=" * 50)
print("🤖 SMART AI RECOMMENDATION SYSTEM")
print("=" * 50)




items = {
    "Python Programming": ["python", "coding", "ai", "automation"],
    "Java Programming": ["java", "coding", "backend"],
    "Web Development": ["html", "css", "javascript", "frontend"],
    "Machine Learning": ["ai", "python", "data"],
    "Data Science": ["python", "data", "analytics"],
    "Cyber Security": ["security", "network", "hacking"],
    "Cloud Computing": ["cloud", "aws", "devops"],
    "Mobile App Development": ["android", "java", "flutter"],
    "UI UX Design": ["design", "figma", "creativity"],
    "Game Development": ["unity", "gaming", "csharp"],
    "DevOps": ["docker", "linux", "cloud"],
    "Blockchain": ["crypto", "security", "coding"],
    "Artificial Intelligence": ["ai", "python", "automation"],
    "Robotics": ["ai", "electronics", "automation"],
    "Computer Vision": ["ai", "opencv", "python"]
}

name = input("Enter your name: ")

print("\nChoose your interests.")
print("Example: python ai coding")

user_input = input("Your interests: ").lower()

user_interests = set(user_input.split())
scores = {}

for item, tags in items.items():

    common = user_interests.intersection(tags)

    score = len(common)

    if score > 0:
        percentage = (score / len(tags)) * 100

        scores[item] = round(percentage, 1)

print("\n" + "=" * 50)

print(f"🎯 Hello {name}")

if scores:

    sorted_scores = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\n⭐ Top Recommendations:\n")

    for i, (item, score) in enumerate(sorted_scores[:5], start=1):

        print(f"{i}. {item}")

        print(f"   Match: {score}%")

else:

    print("\n❌ No recommendations found.")

print("\nThank you for using Smart AI Recommendation System 🤖")