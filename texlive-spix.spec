%global tl_name spix
%global tl_revision 65050

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.0
Release:	%{tl_revision}.1
Summary:	Yet another TeX compilation tool: simple, human readable, no option, no magic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/spix
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spix.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(spix.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
SpiX offers a way to store information about the compilation process for
a tex file inside the tex file itself. Just write the commands as
comments in the tex files, and SpiX will extract and run those commands.
Everything is stored in the tex file (so that you are not missing some
piece of information that is located somewhere else), in a human-
readable format (no need to know SpiX to understand it).

