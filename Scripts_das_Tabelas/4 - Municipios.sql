USE [TESTE]
GO

/****** Object:  Table [dbo].[MUNICIPIOS]    Script Date: 03/06/2021 15:37:25 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[MUNICIPIOS](
	[id] [int] NOT NULL,
	[nome] [varchar](70) NULL,
	[estado] [int] NULL,
	[mesorregiao] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[MUNICIPIOS]  WITH CHECK ADD FOREIGN KEY([estado])
REFERENCES [dbo].[ESTADOS] ([id])
GO

ALTER TABLE [dbo].[MUNICIPIOS]  WITH CHECK ADD FOREIGN KEY([mesorregiao])
REFERENCES [dbo].[MESORREGIOES] ([id])
GO

