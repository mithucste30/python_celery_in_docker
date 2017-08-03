from tasks import add
result = add.apply_async((4, 4), countdown=10)

print(result.get())