import matplotlib.pyplot as plt
from matplotlib import rcParams
from PIL import Image, ImageChops
from os import mkdir
from os.path import exists


def trim(im2):
    bg = Image.new(im2.mode, im2.size, im2.getpixel((0, 0)))
    diff = ImageChops.difference(im2, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    return im2.crop(bbox)


def latex2jpg(latex, jpgname):
    config = {
        "font.family": 'serif',
        "mathtext.fontset": 'stix',
        "font.serif": ['SimSun']
    }
    rcParams.update(config)
    fig = plt.figure(figsize=(20, 10), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    str_latex = '$' + latex + '$'
    plt.text(0.5, 0.5, str_latex, fontsize=10, verticalalignment='center', horizontalalignment='center')
    plt.axis('off')
    path = 'images'
    if not exists(path):
        mkdir(path)
    plt.savefig(f'{path}/{jpgname}.jpg')
    im = Image.open(f'{path}/{jpgname}.jpg')
    im = trim(im)
    im.save(f'{path}/{jpgname}.jpg')


def main():
    latex2jpg(r'J_\alpha(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! \Gamma (m + \alpha + 1)} {\left({ \frac{x}{2} }\right)}^{2m + \alpha}', 'latex1')
    latex2jpg(r'E=mc^2', 'latex2')
    latex2jpg(r'x^{y^z}=(1+{\rm e}^x)^{-2xy^w}', 'latex3')
    latex2jpg(r'f(x,y,z) = 3y^2z \left( 3+\frac{7x+5}{1+y^2} \right)', 'latex4')
    latex2jpg(r'\left. \frac{{\rm d}u}{{\rm d}x} \right| _{x=0}', 'latex5')
    latex2jpg(r'\frac{a-1}{b-1}', 'latex6')
    latex2jpg(r'\sqrt{2}', 'latex7')
    latex2jpg(r'\vec{a} \cdot \vec{b}=0', 'latex8')
    latex2jpg(r'\overleftarrow{xy} \quad and \quad \overleftrightarrow{xy} \quad and \quad \overrightarrow{xy}', 'latex9')
    latex2jpg(r'\int_0^1 {x^2} \,{\rm d}x', 'latex10')
    latex2jpg(r'\lim_{n \to +\infty} \frac{1}{n(n+1)} \quad and \quad \lim_{x\leftarrow{n}} \frac{1}{n(n+1)}', 'latex11')
    latex2jpg(r'\sum_{i=1}^n \frac{1}{i^2} \quad and \quad \prod_{i=1}^n \frac{1}{i^2} \quad and \quad \bigcup_{i=1}^{2} R', 'latex12')
    latex2jpg(r'\alpha\gamma\epsilon\eta\iota\lambda\nu', 'latex13')


if __name__ == '__main__':
    main()
