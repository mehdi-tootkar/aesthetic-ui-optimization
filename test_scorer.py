from server.evaluator.aesthetic import AestheticScorer

with open("ui_test.png", "rb") as f:
    img_bytes = f.read()

scorer = AestheticScorer()
print(scorer.score(img_bytes))
