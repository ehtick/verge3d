#!/usr/bin/env python3
# coding: UTF-8
import sys
l11l1_opy_ = sys.version_info [0] == 2
l1l11_opy_ = 2048
l1ll1l_opy_ = 7
def l111l_opy_ (keyedStringLiteral):
    global l11ll_opy_
    stringNr = ord (keyedStringLiteral [-1])
    rotatedStringLiteral = keyedStringLiteral [:-1]
    rotationDistance = stringNr % len (rotatedStringLiteral)
    recodedStringLiteral = rotatedStringLiteral [:rotationDistance] + rotatedStringLiteral [rotationDistance:]
    if l11l1_opy_:
        stringLiteral = unicode () .join ([unichr (ord (char) - l1l11_opy_ - (charIndex + stringNr) % l1ll1l_opy_) for charIndex, char in enumerate (recodedStringLiteral)])
    else:
        stringLiteral = str () .join ([chr (ord (char) - l1l11_opy_ - (charIndex + stringNr) % l1ll1l_opy_) for charIndex, char in enumerate (recodedStringLiteral)])
    return eval (stringLiteral)
import os, sys, re
l11_opy_ = 40 + 1 + 9 + 4
l111_opy_ = 0xFFFF
l1l1_opy_ = re.compile(l111l_opy_ (u"ࠫࡤࡥࡖ࠴ࡆࡏࡣࡤ࠮࡛ࡢ࠯ࡩࡅ࠲ࡌ࠰࠮࠻ࡠࡿ࠶࠶ࠬ࠲࠲ࢀ࠭ࠬࠀ"))
def l1lll_opy_():
    print(l111l_opy_ (u"ࠬ࠭ࠧࠋࡗࡶࡥ࡬࡫࠺ࠡ࡭ࡨࡽࡲࡧ࡮ࡢࡩࡨࡶ࠳ࡶࡹࠡࡅࡒࡑࡒࡇࡎࡅࠢ࠱࠲࠳ࠐࠊࡂࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡧࡴࡳ࡭ࡢࡰࡧࡷࠥ࠮ࡡ࡭࡮ࠣࡴࡦࡸࡡ࡮ࡵࠣࡥࡷ࡫ࠠࡳࡧࡴࡹ࡮ࡸࡥࡥࠫ࠽ࠎࠏࠦࠠࠡࠢࡤࡧࡹ࡯ࡶࡢࡶࡨࠤࡕࡇࡔࡉࠢࡎࡉ࡞ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡥࡷ࡭ࡻࡧࡴࡦࠢࡨࡲ࡬࡯࡮ࡦࠢࡵࡹࡳࡺࡩ࡮ࡧࠣࡱࡴࡪࡵ࡭ࡧࠣࠬࡪ࠴ࡧ࠯ࠢࡹ࠷ࡩ࠴ࡪࡴࠫࠣࡻ࡮ࡺࡨࠡࡶ࡫ࡩࠥࡹࡰࡦࡥ࡬ࡪ࡮࡫ࡤࠡ࡭ࡨࡽ࠳ࠐࠊࠡࠢࠣࠤࡩ࡫ࡡࡤࡶ࡬ࡺࡦࡺࡥࠡࡒࡄࡘࡍࠐࠠࠡࠢࠣࠤࠥࠦࠠࡅࡧࡤࡧࡹ࡯ࡶࡢࡶࡨࠤࡪࡴࡧࡪࡰࡨࠤࡷࡻ࡮ࡵ࡫ࡰࡩࠥࡳ࡯ࡥࡷ࡯ࡩࠥࡨࡹࠡࡴࡨࡱࡴࡼࡩ࡯ࡩࠣࡸ࡭࡫ࠠ࡬ࡧࡼࠤࡺࡹࡥࡥࠢࡩࡳࡷࠦࡡࡤࡶ࡬ࡺࡦࡺࡩࡰࡰ࠱ࠎࠏࠦࠠࠡࠢࡹࡩࡷ࡯ࡦࡺࠢࡓࡅ࡙ࡎࠊࠡࠢࠣࠤࠥࠦࠠࠡࡘࡨࡶ࡮࡬ࡹࠡࡶ࡫ࡩࠥࡧࡣࡵ࡫ࡹࡥࡹ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡲࡪࠥࡺࡨࡦࠢࡨࡲ࡬࡯࡮ࡦࠢࡵࡹࡳࡺࡩ࡮ࡧࠣࡱࡴࡪࡵ࡭ࡧ࠯ࠤࡵࡸࡩ࡯ࡶࡶࠤࠧࡕࡋࠣࠢࡲࡶࠥࠨࡂࡂࡆࠥ࠲ࠏࠐࠠࠡࠢࠣࡧ࡭࡫ࡣ࡬࠯࡮ࡩࡾࠦࡋࡆ࡛ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡛ࡧ࡬ࡪࡦࡤࡸࡪࠦࡴࡩࡧࠣ࡫࡮ࡼࡥ࡯ࠢ࡮ࡩࡾ࠲ࠠࡱࡴ࡬ࡲࡹࡹࠠࠣࡑࡎࠦࠥࡵࡲࠡࠤࡅࡅࡉࠨ࠮ࠋࠩࠪࠫࠁ"))
def l1l1l_opy_(key):
    if len(key) != l11_opy_:
        return False
    sum = 0
    for i in range(len(key) - 4):
        sum = sum + ord(key[i])
    l1ll1_opy_ = sum % l111_opy_
    l1lll1_opy_ = int(key[len(key)-4 : ], 16)
    return l1ll1_opy_ == l1lll1_opy_
def l1ll_opy_(path):
    with open(path, l111l_opy_ (u"࠭ࡲࠨࠂ"), encoding=l111l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ࠃ")) as l11l_opy_:
        file = l11l_opy_.read()
        match = l1l1_opy_.search(file)
        if match and match.group(1) != l111l_opy_ (u"ࠨ࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴ࠬࠄ"):
            return True
        else:
            return False
def check_key(key):
    return l1l1l_opy_(key)
def checkKey(key):
    return l1l1l_opy_(key)
def activate(path, key, l1111_opy_=True):
    if l1111_opy_ and not l1l1l_opy_(key):
        return False
    ll_opy_ = l111l_opy_ (u"ࠩࡢࡣ࡛࠹ࡄࡍࡡࡢࠫࠅ") + key[0:10]
    file = None
    with open(path, l111l_opy_ (u"ࠪࡶࠬࠆ"), encoding=l111l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪࠇ")) as l11l_opy_:
        file = l11l_opy_.read()
    with open(path, l111l_opy_ (u"ࠬࡽࠧࠈ"), encoding=l111l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬࠉ"), newline=l111l_opy_ (u"ࠧ࡝ࡰࠪࠊ")) as l1_opy_:
        l1_opy_.write(l1l1_opy_.sub(ll_opy_, file))
    return True
def deactivate(path):
    return activate(path, l111l_opy_ (u"ࠨ࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴ࠬࠋ"), False)
if __name__ == l111l_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫࠌ"):
    l1llll_opy_ = sys.argv
    if len(l1llll_opy_) < 3:
        l1lll_opy_()
        sys.exit(1)
    else:
        l1l_opy_ = l1llll_opy_[1]
        if (l1l_opy_ == l111l_opy_ (u"ࠪࡧ࡭࡫ࡣ࡬࠯࡮ࡩࡾ࠭ࠍ") or l1l_opy_ == l111l_opy_ (u"ࠫࡨ࡮ࡥࡤ࡭ࡢ࡯ࡪࡿࠧࠎ")) and len(l1llll_opy_) == 3:
            if l1l1l_opy_(l1llll_opy_[2]):
                print(l111l_opy_ (u"ࠬࡕࡋࠨࠏ"))
                sys.exit(0)
            else:
                print(l111l_opy_ (u"࠭ࡂࡂࡆࠪࠐ"))
                sys.exit(1)
        elif l1l_opy_ == l111l_opy_ (u"ࠧࡷࡧࡵ࡭࡫ࡿࠧࠑ") and len(l1llll_opy_) == 3:
            if l1ll_opy_(l1llll_opy_[2]):
                print(l111l_opy_ (u"ࠨࡑࡎࠫࠒ"))
                sys.exit(0)
            else:
                print(l111l_opy_ (u"ࠩࡅࡅࡉ࠭ࠓ"))
                sys.exit(1)
        elif l1l_opy_ == l111l_opy_ (u"ࠪࡥࡨࡺࡩࡷࡣࡷࡩࠬࠔ") and len(l1llll_opy_) == 4:
            activate(l1llll_opy_[2], l1llll_opy_[3])
            sys.exit(0)
        elif l1l_opy_ == l111l_opy_ (u"ࠫࡩ࡫ࡡࡤࡶ࡬ࡺࡦࡺࡥࠨࠕ") and len(l1llll_opy_) == 3:
            deactivate(l1llll_opy_[2])
            sys.exit(0)
        else:
            sys.exit(1)