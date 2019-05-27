import moduleFoo

print("moduleBar's __name__ = %s" % __name__)

if __name__ == "__main__":
    print("moduleBar is being run directly")
else:
    print("moduleBar is being imported")

