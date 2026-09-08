import time
import sys

# Change this to your sister's name
sister = "Dear chitti thalli"


def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Opening
print("\n" + "❤️ " * 10)
type_text("        💖 A SPECIAL MESSAGE FOR MY SISTER 💖", 0.04)
print("❤️ " * 10)

time.sleep(1)

type_text(f"\nDear {sister},", 0.06)
time.sleep(0.5)

type_text("\n🎂 HAPPY BIRTHDAY, SIS! 🎂", 0.08)
type_text("🥳🎉🎁💐✨❤️", 0.08)

time.sleep(1)

type_text("\nI also want to say something from my heart...", 0.04)
time.sleep(0.8)

type_text("\n🙏 I'M REALLY SORRY 🙏", 0.08)

type_text(
    "\nIf I have hurt you or made you upset, "
    "I'm truly sorry.",
    0.035
)

type_text(
    "I never wanted to hurt you, "
    "and I hope you can forgive me. ❤️",
    0.035
)

time.sleep(0.8)

type_text("\nYou are not just my sister...", 0.04)
type_text("You are one of the most special people in my life. 💕", 0.04)

time.sleep(0.8)

type_text("\n🌸 On your birthday, I wish you 🌸", 0.05)

wishes = [
    "💖 Lots and lots of happiness",
    "🌟 Success in everything you do",
    "😊 A beautiful smile every day",
    "🌈 Wonderful memories",
    "🎁 All your dreams coming true",
    "❤️ And a life filled with love"
]

for wish in wishes:
    type_text(wish, 0.03)
    time.sleep(0.3)

time.sleep(1)

type_text("\n🎂 HAPPY BIRTHDAY, MY DEAR SISTER! 🎂", 0.07)
type_text("🙏 I'M SORRY. PLEASE FORGIVE ME. ❤️", 0.06)
type_text("🥰 LOVE YOU ALWAYS! 🥰", 0.07)

print("\n" + "💖 " * 10)
