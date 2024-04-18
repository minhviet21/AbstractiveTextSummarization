def freeze(model, block):
    for name, param in model.named_parameters():
        if ("model." + block) in name:
            param.requires_grad = False

def unfreeze_except(model, block):
    for name, param in model.named_parameters():
        if ("model." + block) not in name:
            param.requires_grad = False