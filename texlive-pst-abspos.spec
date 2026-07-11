%global tl_name pst-abspos
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Put objects at an absolute position
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-abspos
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-abspos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-abspos.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-abspos.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The (PSTricks-related) package provides a command \pstPutAbs(x,y) to put
an object at an arbitrary absolute (or even a relative) position on the
page.

