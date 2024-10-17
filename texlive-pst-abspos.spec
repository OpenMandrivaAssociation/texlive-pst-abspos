Name:		texlive-pst-abspos
Version:	15878
Release:	2
Summary:	Put objects at an absolute position
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-abspos
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-abspos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-abspos.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-abspos.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The (PSTricks-related) package provides a command
\pstPutAbs(x,y) to put an object at an arbitrary absolute (or
even a relative) position on the page.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-abspos/pst-abspos.tex
%{_texmfdistdir}/tex/latex/pst-abspos/pst-abspos.sty
%doc %{_texmfdistdir}/doc/generic/pst-abspos/Changes
%doc %{_texmfdistdir}/doc/generic/pst-abspos/README
%doc %{_texmfdistdir}/doc/generic/pst-abspos/pst-abspos-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-abspos/pst-abspos-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-abspos/pst-abspos-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-abspos/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
