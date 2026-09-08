import random

secret_number = random.randint(1, 100)

valid_guesses = 0
invalid_guesses = 0

print("🎯 مرحباً بك في لعبة التخمين High-Low!")
print("خمن رقماً بين 1 و 100.\n")

while True:
    user_input = input("أدخل تخمينك: ")

    if not user_input.isdigit():
        print("❌ مدخل غير صحيح! يرجى إدخال رقم صحيح فقط.\n")
        invalid_guesses += 1
        continue

    guess = int(user_input)

    if guess < 1 or guess > 100:
        print("⚠️ الرقم خارج النطاق! يرجى إدخال رقم بين 1 و 100.\n")
        invalid_guesses += 1
        continue

    valid_guesses += 1

    if guess < secret_number:
        print("📈 قليل جداً! (Too low)\n")
    elif guess > secret_number:
        print("📉 كبير جداً! (Too high)\n")
    else:
        print("🎉 مبروك! إجابة صحيحة!")
        break

total_guesses = valid_guesses + invalid_guesses

print("\n--- 📊 ملخص اللعبة ---")
print(f"المحاولات الصالحة: {valid_guesses}")
print(f"المحاولات غير الصالحة: {invalid_guesses}")
print(f"إجمالي المحاولات: {total_guesses}")
