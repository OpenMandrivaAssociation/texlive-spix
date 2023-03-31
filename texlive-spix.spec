Name:		texlive-spix
Version:	55933
Release:	2
Summary:	Yet another TeX compilation tool: simple, human readable, no option, no magic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spix
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spix.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
SpiX offers a way to store information about the compilation
process for a tex file inside the tex file itself. Just write
the commands as comments in the tex files, and SpiX will
extract and run those commands. Everything is stored in the tex
file (so that you are not missing some piece of information
that is located somewhere else), in a human-readable format (no
need to know SpiX to understand it).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/spix
%doc %{_texmfdistdir}/texmf-dist/doc/support/spix
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/spix.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/spix.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
