import rgb

# Generally needed code:
FRAME_WIDTH = 32
FRAME_HEIGHT = 8

# Note that this is split up to make it easier to copy-paste to the cli
tree_img = []
tree_img += [
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0xc2f8e3ff, 0x40a640ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x42a740ff, 0x41a53fff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x8bc69fff, 0x43a841ff, 0x47a93fff, 0x7dcba4ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x399f3aff, 0x40a940ff, 0xc6e2c1ff, 0x34a647ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x67b86eff, 0x44b58fff, 0x4bb896ff, 0xacd2a6ff, 0x40a740ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x3da641ff, 0x36a463ff, 0x3aa864ff, 0x43a741ff, 0x42a642ff, 0x459d50ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x499d4dff, 0x42a83fff, 0x3ea43eff, 0x41a842ff, 0x40a941ff, 0xb7522dff, 0x3ca241ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x35903fff, 0x3fa73cff, 0x46a841ff, 0x41a642ff, 0x379b39ff, 0x41a843ff, 0xed2b23ff, 0xcc3b27ff, 0x3b933fff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
]
tree_img += [
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0xf6f250ff, 0x3da643ff, 0xfffefaff, 0x40a541ff, 0x41a543ff, 0x44a942ff, 0x40a841ff, 0x47a73eff, 0x3ba03eff, 0x3c9b40ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x46aa48ff, 0x42a63eff, 0xf6ad47ff, 0x23a03bff, 0x40a641ff, 0x44a841ff, 0x3fa43dff, 0x55c4ecff, 0x43a641ff, 0x389939ff, 0x42a642ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x40a541ff, 0x3ca03eff, 0x44a741ff, 0xf28441ff, 0xf7ef4aff, 0x42a743ff, 0x1fa33fff, 0x47aa48ff, 0x3fa842ff, 0x42a744ff, 0x3fa742ff, 0x3aa240ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x42a245ff, 0xee2825ff, 0x40a440ff, 0x41a643ff, 0x3fa53eff, 0x3fa23fff, 0xfdf24cff, 0xfdf34dff, 0x42a840ff, 0x44a741ff, 0x41a840ff, 0x3ba23fff, 0xfaf34dff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x45a243ff, 0x41a644ff, 0x43a740ff, 0x3ca03eff, 0x40a841ff, 0x45a944ff, 0x47a944ff, 0x4baa43ff, 0x42a641ff, 0xf9b048ff, 0xfcb24cff, 0xf17c48ff, 0xfbf049ff, 0x46a63cff, 0x4da03fff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x4aa243ff, 0x3ba03cff, 0x3fa642ff, 0x3aa23dff, 0x60c8f3ff, 0x5fc7f8ff, 0x42a63fff, 0x43a73fff, 0x43a840ff, 0x40a842ff, 0x4aa943ff, 0x44a143ff, 0x48a539ff, 0x3ba03aff, 0x389a38ff, 0x379938ff, 0x469940ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x3ba640ff, 0x42a743ff, 0x40a742ff, 0xfcfef8ff, 0x3ea440ff, 0x41a53eff, 0x41a541ff, 0x40a740ff, 0x379c3bff, 0x41a842ff, 0xec2926ff, 0xf02d28ff, 0x41a743ff, 0x44a83fff, 0xfbfefbff, 0x3fa542ff, 0x40a641ff, 0x369838ff, 0x349c3bff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x3fa641ff, 0x3fa840ff, 0x3fa644ff, 0x46a743ff, 0x46a946ff, 0x41a743ff, 0x41a843ff, 0x41a843ff, 0xed2924ff, 0xea2b26ff, 0x41a643ff, 0x43a742ff, 0x41aa40ff, 0x41a742ff, 0x41a843ff, 0x40a842ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
]
tree_img += [
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x3b9d3aff, 0x41a741ff, 0x41a943ff, 0xfdfdfaff, 0x40a842ff, 0x40a842ff, 0x48a840ff, 0x48a73fff, 0x44a742ff, 0x41a743ff, 0x3c9f3cff, 0x359a3aff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x34973aff, 0x35973aff, 0x3b9f3dff, 0x359839ff, 0x339739ff, 0x369937ff, 0x359938ff, 0x3c9e3aff, 0x36973aff, 0x3da13cff, 0x369a38ff, 0x379938ff, 0x3d9e3eff, 0x35973fff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x3b9e39ff, 0x36983bff, 0x3b9e3dff, 0x37993aff, 0x359a39ff, 0x42a445ff, 0x41a642ff, 0x36983aff, 0x3b9e3fff, 0x40a443ff, 0x3ca03eff, 0x36983bff, 0x3b9f3fff, 0x35993aff, 0x369739ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0xfaaf42ff, 0x3ca13dff, 0x3da13fff, 0x40a845ff, 0x40a843ff, 0x41a643ff, 0x3ca13eff, 0x3ca03cff, 0x45a742ff, 0x40a843ff, 0x3ca03eff, 0x3ca03eff, 0x37983aff, 0x3ca03cff, 0x3ea640ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x3b9e3bff, 0x3c9f41ff, 0xfaef45ff, 0x3fa63fff, 0x40a743ff, 0x41a843ff, 0xfffefeff, 0x40a741ff, 0x46a843ff, 0x42a841ff, 0x56cbf4ff, 0x56ccf3ff, 0x43a844ff, 0x3fa744ff, 0x3ca03eff, 0x3ca03eff, 0x36983fff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x41a944ff, 0x3ba03cff, 0x47a73dff, 0xf57d46ff, 0xfbb144ff, 0xfaed44ff, 0x47aa40ff, 0x44a73cff, 0x41a740ff, 0x41a843ff, 0x42a842ff, 0x58cbf2ff, 0x40a743ff, 0xfefffeff, 0x43a740ff, 0x3ca03eff, 0x379a3eff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x40a743ff, 0x3b9e3bff, 0xed2b23ff, 0xec2b24ff, 0x47aa3fff, 0x3ea841ff, 0x40a944ff, 0xfaee47ff, 0xfbf049ff, 0xfbf048ff, 0x41a843ff, 0x20a343ff, 0x399c3fff, 0x3fa742ff, 0x4aa840ff, 0x46a83fff, 0xf8ef48ff, 0xfab048ff, 0x339739ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x3da642ff, 0x3b9f3dff, 0x3da13dff, 0x42a642ff, 0xec2b24ff, 0x40a642ff, 0x40a843ff, 0x47a840ff, 0x3fa740ff, 0x40a644ff, 0x3fa742ff, 0xfdf04aff, 0xfab04aff, 0xfbb24bff, 0xf37f3fff, 0xfdf148ff, 0xfbf049ff, 0x3fa742ff, 0x42a542ff, 0x3c9e3bff, 0x379a3eff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
]
tree_img += [
    0x000000ff, 0x000000ff, 0x000000ff, 0x3fa942ff, 0x3b9d3aff, 0x3d9e3fff, 0x47a943ff, 0x40a843ff, 0x42a743ff, 0x1fa440ff, 0x3ea842ff, 0x41a843ff, 0x43a743ff, 0x41a843ff, 0x41a843ff, 0x41a843ff, 0x42a944ff, 0x41a843ff, 0x48a83fff, 0x48a842ff, 0x48a940ff, 0x42a744ff, 0x40a943ff, 0x43a743ff, 0xfefefdff, 0x3da13aff, 0x3da13dff, 0x37993dff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x3ca73eff, 0x3ba03cff, 0x40aa44ff, 0x3fa744ff, 0x3ba03cff, 0x41a842ff, 0x41a843ff, 0x43a83fff, 0x41a742ff, 0x41a843ff, 0x42a743ff, 0x45a841ff, 0x41a742ff, 0x379a39ff, 0x40a643ff, 0x41a843ff, 0x42a943ff, 0x41a842ff, 0x41a842ff, 0x40a843ff, 0x36983aff, 0x46a842ff, 0x42a844ff, 0x58c9f8ff, 0x3fa842ff, 0x3ca03dff, 0x36993eff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x40a642ff, 0x21a442ff, 0x40a742ff, 0x41a745ff, 0xfefcfdff, 0x40a73eff, 0x41a843ff, 0x3ba03bff, 0x56cdf3ff, 0x40a742ff, 0x20a443ff, 0x24a345ff, 0xfefffaff, 0x41a843ff, 0x41a843ff, 0xef2924ff, 0xef2824ff, 0x3fa943ff, 0x41a642ff, 0x41a843ff, 0x47a841ff, 0x48ab41ff, 0x42a642ff, 0x41a742ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x41a742ff, 0x21a544ff, 0x1fa445ff, 0x40a644ff, 0x41a843ff, 0x54cbf4ff, 0x55ccf6ff, 0x40a743ff, 0x40a743ff, 0x41a741ff, 0x40a840ff, 0x45a841ff, 0x47a640ff, 0x49a741ff, 0x3fa643ff, 0x40a843ff, 0x41a843ff, 0x41a843ff, 0x41a943ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x389a3cff, 0x3c9d3aff, 0x41a741ff, 0x48a742ff, 0x40a841ff, 0x3fa842ff, 0x45a742ff, 0x41a740ff, 0x21a346ff, 0x47a842ff, 0x42a743ff, 0x43a743ff, 0x44a83fff, 0x42a541ff, 0x3c9f3eff, 0x37993aff, 0x37973cff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x40a741ff, 0x3c9f3cff, 0x3ca03bff, 0x37993bff, 0x3b9f3dff, 0x359a3aff, 0x3c9f3dff, 0x46a842ff, 0x39983dff, 0x369939ff, 0x3ca03dff, 0x36973bff, 0x379939ff, 0x3b9f3dff, 0x36993bff, 0x37983cff, 0x37973cff, 0x399f3bff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0xf9b246ff, 0xfbf04eff, 0x40a742ff, 0x3b9e40ff, 0x3a9e3cff, 0x40a842ff, 0x36993aff, 0x3ca03eff, 0x379a3bff, 0x3b9f3dff, 0x37983cff, 0x3c9f3eff, 0x3ca03eff, 0x3ca03eff, 0x3ca03eff, 0x3ca03eff, 0x3ca03eff, 0x41a843ff, 0x3ba03eff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x43a543ff, 0x3ba03dff, 0x3fa640ff, 0xfbf048ff, 0x3ba03dff, 0x40a742ff, 0x41a843ff, 0x41a843ff, 0x42a743ff, 0x42a743ff, 0x369a3aff, 0x3ca03eff, 0x43a543ff, 0x41a843ff, 0x41a843ff, 0x3ba23fff, 0x35993aff, 0x37973cff, 0x41a843ff, 0x3ca03eff, 0x34993aff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
]
tree_img += [
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x43a545ff, 0x36983bff, 0x41a843ff, 0x40a843ff, 0xfdf045ff, 0xfab247ff, 0xf37e3fff, 0xfef147ff, 0x349a40ff, 0x41a941ff, 0x41a840ff, 0x41a940ff, 0x47a541ff, 0x41a844ff, 0x40a944ff, 0xfcffffff, 0x42a641ff, 0x41a843ff, 0x41a743ff, 0x37983eff, 0x3ca03bff, 0xfbb149ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x44a842ff, 0x369a3aff, 0x42a742ff, 0x41a742ff, 0x41a742ff, 0x40a742ff, 0x41a843ff, 0x36993aff, 0x3fa744ff, 0xfdee43ff, 0xf9ef4aff, 0xf8f14aff, 0xfab245ff, 0xf47e42ff, 0xfced47ff, 0x40a744ff, 0x3ba140ff, 0x3c9f3cff, 0x40a842ff, 0xfbf147ff, 0xfab144ff, 0xfaf347ff, 0x3d9f40ff, 0x3c9e3dff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x42a642ff, 0x3da03dff, 0x40a843ff, 0x3fa842ff, 0x47a842ff, 0x55cbf4ff, 0x45a742ff, 0x42a844ff, 0x43a841ff, 0x3fa742ff, 0x41a743ff, 0x47a843ff, 0x41a741ff, 0x3b9f3dff, 0x40a742ff, 0x41a642ff, 0xfcef4bff, 0xfcae42ff, 0xf47e3eff, 0xfab144ff, 0x40a742ff, 0x369839ff, 0x43a743ff, 0x379b3bff, 0x57caf5ff, 0x36983bff, 0x21a141ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x23a341ff, 0x3b9f3eff, 0x3ca03eff, 0xee2b24ff, 0x3b9f3bff, 0x40a742ff, 0x41a742ff, 0x40a641ff, 0x40a742ff, 0xfafefbff, 0x3b9f3aff, 0x41a843ff, 0x42a743ff, 0x47a942ff, 0x41a642ff, 0x41a842ff, 0x47a63fff, 0x42a743ff, 0x41a843ff, 0x41a843ff, 0x41a843ff, 0x41a843ff, 0x41a843ff, 0x40a742ff, 0x48a841ff, 0x3b9f3cff, 0xfdfefeff, 0x3c9f3fff, 0x369839ff, 0x38a041ff, 0x000000ff,
    0x1fa441ff, 0x3b9f3cff, 0x3aa03cff, 0x3fa541ff, 0x3c9f3cff, 0x3b9f3eff, 0x3aa03eff, 0x3da13bff, 0x36983bff, 0x41a642ff, 0x46a942ff, 0x47a942ff, 0x49a742ff, 0x48a842ff, 0x47a842ff, 0x41a742ff, 0x47a740ff, 0xfcfffdff, 0x46a941ff, 0x47a941ff, 0x40a843ff, 0x47a942ff, 0x41a843ff, 0x3ba03cff, 0xeb2b23ff, 0x46a841ff, 0x40a841ff, 0x3fa641ff, 0x40a744ff, 0x349938ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x43a642ff, 0x20a242ff, 0x42a441ff, 0x21a442ff, 0x3aa03dff, 0xfafffaff, 0x3d9f3cff, 0x40a541ff, 0x41a842ff, 0x46a842ff, 0xed2b23ff, 0xeb2b24ff, 0x40a73fff, 0x47a942ff, 0x48a942ff, 0x43a643ff, 0x3fa642ff, 0x57c8f5ff, 0x41a843ff, 0x41a843ff, 0x3da13fff, 0x3ca03eff, 0xf22926ff, 0xec2c25ff, 0x389837ff, 0x389837ff, 0x42a73eff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x1fa245ff, 0x3fa546ff, 0x3fa544ff, 0x3c9f3dff, 0x40a843ff, 0x40a843ff, 0x3aa03dff, 0xf12a26ff, 0xef2a24ff, 0x3fa841ff, 0x38a13dff, 0x3ca03dff, 0x3ba03cff, 0x54c9f4ff, 0x59c9f2ff, 0x43a840ff, 0xfcfff9ff, 0x42a642ff, 0x3fa844ff, 0x24a345ff, 0x42a542ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x40a643ff, 0x3fa641ff, 0x40a742ff, 0x40a742ff, 0x47aa40ff, 0x22a243ff, 0x41a643ff, 0x21a444ff, 0x3fa645ff, 0x40a546ff, 0x20a147ff, 0x40a740ff, 0x40a742ff, 0x3ea640ff, 0x21a241ff, 0x20a344ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
]
tree_img += [
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x593612ff, 0x5e3611ff, 0x5e3511ff, 0x593811ff, 0x5d3511ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x5c350dff, 0x653d16ff, 0x5e3511ff, 0x653d17ff, 0x6e441bff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x5f350eff, 0x643d15ff, 0x5c3711ff, 0x6c431dff, 0x653d16ff, 0x653c16ff, 0x73431aff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
    0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x633b10ff, 0x5d360dff, 0x6e421bff, 0x704218ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff, 0x000000ff,
]


def render(delay):
    tree_img_width = 32
    tree_img_height = len(tree_img) // tree_img_width
    img_pos_y = FRAME_HEIGHT
    img_pos_y_speed = -1
    txt_pos_x = 0
    top_txt = 'Welcome'
    top_txt_width = rgb.textwidth(top_txt)
    bottom_txt = 'Dear Guests'
    bottom_txt_width = rgb.textwidth(bottom_txt)

    def fn():
        nonlocal img_pos_y, img_pos_y_speed, txt_pos_x
        rgb.clear()
        rgb.text(top_txt, pos=(txt_pos_x, img_pos_y - FRAME_HEIGHT))
        rgb.image(tree_img, pos=(0, img_pos_y), size=(
            tree_img_width, tree_img_height))
        rgb.text(bottom_txt, pos=(txt_pos_x, tree_img_height + img_pos_y))
        if img_pos_y >= FRAME_HEIGHT:
            # at the top, so check if text needs to be scrolled
            if top_txt_width + txt_pos_x > FRAME_WIDTH:
                # top text doesn't fit, so scroll it before moving down again
                img_pos_y_speed = 0
                txt_pos_x -= 1
            else:
                img_pos_y_speed = -1
                if txt_pos_x < 0:
                    txt_pos_x += 1
        elif img_pos_y <= -tree_img_height:
            # at the bottom, so check if text needs to be scrolled
            if bottom_txt_width + txt_pos_x > FRAME_WIDTH:
                # bottom text doesn't fit, so scroll it before moving up again
                img_pos_y_speed = 0
                txt_pos_x -= 1
            else:
                img_pos_y_speed = 1
                if txt_pos_x < 0:
                    txt_pos_x += 1
        else:
            # somehere in the middle, so scroll the text back, if needed
            if txt_pos_x < 0:
                txt_pos_x += 1
        img_pos_y += img_pos_y_speed
        return delay
    return fn


virtualtimers.begin(100)
virtualtimers.new(0, render(200))