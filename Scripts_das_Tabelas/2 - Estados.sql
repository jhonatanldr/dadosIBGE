USE [TESTE]
GO

/****** Object:  Table [dbo].[ESTADOS]    Script Date: 03/06/2021 15:31:47 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[ESTADOS](
	[id] [int] NOT NULL,
	[sigla] [varchar](2) NOT NULL,
	[nome] [varchar](30) NOT NULL,
	[regiao] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[ESTADOS]  WITH CHECK ADD FOREIGN KEY([regiao])
REFERENCES [dbo].[REGIOES] ([id])
GO

